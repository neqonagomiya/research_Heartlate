/* monoplay.c */

// clang monoplay2.c -o monoplay2 /usr/local/Cellar/portaudio/19.6.0/lib/libportaudio.a -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <portaudio.h>
#include "FileLib_osx.h"

/* #define SAMPLE_RATE  (17932) // Test failure to open with this value. */
#define SAMPLE_RATE  (48000)
#define FRAMES_PER_BUFFER (1024)
#define NUM_CHANNELS    (1)
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
    int i, n;

    short int *write_buffer;
    short int *data;
    unsigned int len;
    double *rec_raw_data;
    double *ddata;
    int NUM_REPETITION;
    int DOUKI_START;
    char *filename;
    FILE *fp;


    if (argc != 2) {
        fprintf(stderr, "lack of arguments.\n");
        fprintf(stderr, "monoplay monaural_audio_file(.DXX)\n");
        exit(EXIT_FAILURE);
    }
    filename = argv[1];

    fprintf(stderr, "PROGRAM START.\n");
    fflush(stdout);

    write_buffer = (short int *) malloc(sizeof(short int) * FRAMES_PER_BUFFER);
    if (write_buffer == NULL) exit(-1);

    fprintf(stderr, "Reading audio data file:%s.\n", filename);

    len = lenfile(filename);
    fprintf(stderr, "length:%d\n", len);


    ddata = (double *) malloc(sizeof(double) * len);
    data = (short int *) malloc(sizeof(short int) * len);
    if ((ddata == NULL) && (data == NULL)) exit(-1);
    AnyFileRead(filename, ddata, len);
    for (n = 0; n < len; n++) data[n] = (short int) ddata[n];

    fprintf(stderr, "Initializing portaudio...\n");
    fflush(stdout);
    err = Pa_Initialize();
    if (err != paNoError) goto error;

    outputParameters.device = Pa_GetDefaultOutputDevice(); /* default output device */
    outputParameters.channelCount = NUM_CHANNELS;
    outputParameters.sampleFormat = PA_SAMPLE_TYPE;
    outputParameters.suggestedLatency = Pa_GetDeviceInfo(outputParameters.device)->defaultLowOutputLatency;
    outputParameters.hostApiSpecificStreamInfo = NULL;

    /* -- setup -- */
    fprintf(stderr, "Open the portaudio stream\n");
    fflush(stdout);
    err = Pa_OpenStream(
            &stream,
            NULL,
            &outputParameters,
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


    for (n = 0; n < (int) (len / FRAMES_PER_BUFFER); n++) {
        for (i = 0; i < FRAMES_PER_BUFFER; i++) {
            write_buffer[i] = data[i + n * FRAMES_PER_BUFFER];
        }
        err = Pa_WriteStream(stream, write_buffer, FRAMES_PER_BUFFER);
        if (err && CHECK_UNDERFLOW) goto xrun;
    }


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

