/* birecord.c */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <portaudio.h>
#include "FileLib_osx.h"

/* #define SAMPLE_RATE  (17932) // Test failure to open with this value. */
#define SAMPLE_RATE  (48000)
#define FRAMES_PER_BUFFER (1)


/*Here is difference birecord.c and  monorecord.c*/
#define NUM_CHANNELS    (2)


/* #define DITHER_FLAG     (paDitherOff)  */
#define DITHER_FLAG     (0) /**/

/* @todo Underflow and overflow is disabled until we fix priming of blocking write. */
#define CHECK_OVERFLOW  (0)
#define CHECK_UNDERFLOW  (0)


/* Select sample format. */
#if 0
#define PA_SAMPLE_TYPE  paFloat32
#define SAMPLE_SIZE (4)
#define SAMPLE_SILENCE  (0.0f)
#define CLEAR(a) memset( (a), 0, FRAMES_PER_BUFFER * NUM_CHANNELS * SAMPLE_SIZE )
#define PRINTF_S_FORMAT "%.8f"
#elif 1
#define PA_SAMPLE_TYPE  paInt16
#define SAMPLE_SIZE (2)
#define SAMPLE_SILENCE  (0)
#define CLEAR(a) memset( (a), 0,  FRAMES_PER_BUFFER * NUM_CHANNELS * SAMPLE_SIZE )
#define PRINTF_S_FORMAT "%d"
#elif 0
#define PA_SAMPLE_TYPE  paInt24
#define SAMPLE_SIZE (3)
#define SAMPLE_SILENCE  (0)
#define CLEAR(a) memset( (a), 0,  FRAMES_PER_BUFFER * NUM_CHANNELS * SAMPLE_SIZE )
#define PRINTF_S_FORMAT "%d"
#elif 0
#define PA_SAMPLE_TYPE  paInt8
#define SAMPLE_SIZE (1)
#define SAMPLE_SILENCE  (0)
#define CLEAR(a) memset( (a), 0,  FRAMES_PER_BUFFER * NUM_CHANNELS * SAMPLE_SIZE )
#define PRINTF_S_FORMAT "%d"
#else
#define PA_SAMPLE_TYPE  paUInt8
#define SAMPLE_SIZE (1)
#define SAMPLE_SILENCE  (128)
#define CLEAR( a ) { \
    int i; \
    for( i=0; i<FRAMES_PER_BUFFER*NUM_CHANNELS; i++ ) \
        ((unsigned char *)a)[i] = (SAMPLE_SILENCE); \
}
#define PRINTF_S_FORMAT "%d"
#endif


/*******************************************************************/
int main(int argc, char *argv[]) {
    PaStreamParameters inputParameters, outputParameters;
    PaStream *stream = NULL;
    PaError err;
    int n;

    short int *read_buffer;
    double *rec_raw_data;
    FILE *fp;
    unsigned int len;
    char *filename;
    long int record_sample;

    if (argc != 3) {
        fprintf(stderr, "lack of arguments.\n");
        fprintf(stderr, "monorecord monaural_audio_file(.DXX) record_sample\n");
        exit(EXIT_FAILURE);
    }
    filename = argv[1];
    record_sample = atoi(argv[2]);

    fprintf(stderr, "PROGRAM START.\n");
    fflush(stdout);

    read_buffer = (short int *) malloc(sizeof(short int) * FRAMES_PER_BUFFER);
    if (read_buffer == NULL) exit(EXIT_FAILURE);

    fprintf(stderr, "Writing audio data file:%s.\n", filename);
    fp = fopen(filename, "wb");
    if (fp == NULL) exit(-1);


    fprintf(stderr, "Initializing portaudio...\n");
    fflush(stdout);
    err = Pa_Initialize();
    if (err != paNoError) goto error;

    inputParameters.device = Pa_GetDefaultInputDevice();
    inputParameters.channelCount = NUM_CHANNELS;
    inputParameters.sampleFormat = PA_SAMPLE_TYPE;
    inputParameters.suggestedLatency = Pa_GetDeviceInfo(inputParameters.device)->defaultLowInputLatency;
    inputParameters.hostApiSpecificStreamInfo = NULL;

    /* -- setup -- */
    fprintf(stderr, "Open the portaudio stream\n");
    fflush(stdout);
    err = Pa_OpenStream(
            &stream,
            &inputParameters,
            NULL,
            SAMPLE_RATE,
            FRAMES_PER_BUFFER,
            paClipOff,      /* we won't output out of range samples so don't bother clipping them */
            NULL, /* no callback, use blocking API */
            NULL); /* no callback, so no callback userData */
    if (err != paNoError) goto error;


    fprintf(stderr, "Start the portaudio stream\n");
    fflush(stdout);
    err = Pa_StartStream(stream);
    if (err != paNoError) goto error;


    for (n = 0; n < (int) (record_sample / FRAMES_PER_BUFFER); n++) {
        err = Pa_ReadStream(stream, read_buffer, FRAMES_PER_BUFFER);
        if (err && CHECK_OVERFLOW) goto xrun;
        fwrite(read_buffer, sizeof(short int), FRAMES_PER_BUFFER, fp);
    }
    fclose(fp);

    err = Pa_StopStream(stream);
    if (err != paNoError) goto error;

    Pa_Terminate();
    return 0;

    xrun:
    if (stream) {
        Pa_AbortStream(stream);
        Pa_CloseStream(stream);
    }

    Pa_Terminate();
    if (err & paInputOverflow)
        fprintf(stderr, "Input Overflow.\n");
    if (err & paOutputUnderflow)
        fprintf(stderr, "Output Underflow.\n");
    return -2;

    error:
    if (stream) {
        Pa_AbortStream(stream);
        Pa_CloseStream(stream);
    }

    Pa_Terminate();
    fprintf(stderr, "An error occured while using the portaudio stream\n");
    fprintf(stderr, "Error number: %d\n", err);
    fprintf(stderr, "Error message: %s\n", Pa_GetErrorText(err));
    return -1;
}

