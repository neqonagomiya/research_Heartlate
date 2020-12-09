NO_DEPENDENCY_PROGRAMS=bin/FC_deviation bin/FC_deviation_alter bin/IMPmcode bin/LE_1 bin/WAVtoDSB_osx bin/biascut bin/calc_ILD bin/cosine_windowing bin/cutout_anyfile bin/cutout_anyfile2 bin/douki_new bin/dv bin/equ_schroeder1 bin/equ_schroeder2 bin/equ_schroeder3 bin/equ_schroeder4 bin/equ_schroeder5 bin/fatchdb bin/fff bin/find_cutpoint bin/henkan bin/imp_add bin/imp_add_by10 bin/inverse bin/linear_inpo_hrir_using_ATD bin/mono2LR bin/peaking_filter bin/print_siglen bin/random bin/scaling_max_instant_amp bin/sepach bin/sinwave bin/timeconvo bin/unbias bin/zeropad_anyfile
PORTAUDIO_PROGRAMS=bin/2chplay bin/closed_loop_new bin/monoplay bin/monoplay2 bin/monoplay_48k bin/monoplay_8kHz bin/monoplay_alter bin/monorecord bin/playrec_2ch_inPath bin/playrec_2ch_new_kai bin/playrec_mono bin/playrec_mono_inPath bin/playrec_multi
FFTW_PROGRAMS=bin/fftout2 bin/fftout3 bin/fftout4 bin/make_whitenoise
UMASIG_PROGRAMS=bin/calc_ITD bin/fff bin/linear_inpo_hrir_using_ATD

ALL_PROGRAMS=${NO_DEPENDENCY_PROGRAMS} ${PORTAUDIO_PROGRAMS} ${FFTW_PROGRAMS} ${UMASIG_PROGRAMS}

# if [ ! -d "bin" ]; then mkdir bin; fi
# if [ ! -d "lib" ]; then mkdir lib; fi

.PHONY: all
all: init ${ALL_PROGRAMS}

init: 
	@if [ ! -d "bin" ]; then mkdir bin; fi
	@if [ ! -d "lib" ]; then mkdir lib; fi

install: all
	install -s ${ALL_PROGRAMS} ${HOME}/local/bin

# no dependencies
bin/FC_deviation: FC_deviation.c Filelib_osx.c
	gcc FC_deviation.c Filelib_osx.c -o bin/FC_deviation -I/usr/local/include -lm

bin/FC_deviation_alter: FC_deviation_alter.c Filelib_osx.c
	gcc FC_deviation_alter.c Filelib_osx.c -o bin/FC_deviation_alter -I/usr/local/include -lm

bin/IMPmcode: IMPmcode.c Filelib_osx.c
	gcc IMPmcode.c Filelib_osx.c -o bin/IMPmcode -I/usr/local/include -lm

bin/LE_1: LE_1.c Filelib_osx.c
	gcc LE_1.c Filelib_osx.c -o bin/LE_1 -I/usr/local/include -lm

bin/WAVtoDSB_osx: WAVtoDSB_osx.c Filelib_osx.c
	gcc WAVtoDSB_osx.c Filelib_osx.c -o bin/WAVtoDSB_osx -I/usr/local/include -lm

bin/biascut: biascut.c Filelib_osx.c
	gcc biascut.c Filelib_osx.c -o bin/biascut -I/usr/local/include -lm

bin/calc_ILD: calc_ILD.c Filelib_osx.c
	gcc calc_ILD.c Filelib_osx.c -o bin/calc_ILD -I/usr/local/include -lm

bin/cosine_windowing: cosine_windowing.c Filelib_osx.c
	gcc cosine_windowing.c Filelib_osx.c -o bin/cosine_windowing -I/usr/local/include -lm

bin/cutout_anyfile: cutout_anyfile.c Filelib_osx.c
	gcc cutout_anyfile.c Filelib_osx.c -o bin/cutout_anyfile -I/usr/local/include -lm

bin/cutout_anyfile2: cutout_anyfile2.c Filelib_osx.c
	gcc cutout_anyfile2.c Filelib_osx.c -o bin/cutout_anyfile2 -I/usr/local/include -lm

bin/douki_new: douki_new.c Filelib_osx.c
	gcc douki_new.c Filelib_osx.c -o bin/douki_new -I/usr/local/include -lm

bin/dv: dv.c Filelib_osx.c
	gcc dv.c Filelib_osx.c -o bin/dv -I/usr/local/include -lm

bin/equ_schroeder1: equ_schroeder1.c Filelib_osx.c
	gcc equ_schroeder1.c Filelib_osx.c -o bin/equ_schroeder1 -I/usr/local/include -lm

bin/equ_schroeder2: equ_schroeder2.c Filelib_osx.c
	gcc equ_schroeder2.c Filelib_osx.c -o bin/equ_schroeder2 -I/usr/local/include -lm

bin/equ_schroeder3: equ_schroeder3.c Filelib_osx.c
	gcc equ_schroeder3.c Filelib_osx.c -o bin/equ_schroeder3 -I/usr/local/include -lm

bin/equ_schroeder4: equ_schroeder4.c Filelib_osx.c
	gcc equ_schroeder4.c Filelib_osx.c -o bin/equ_schroeder4 -I/usr/local/include -lm

bin/equ_schroeder5: equ_schroeder5.c Filelib_osx.c
	gcc equ_schroeder5.c Filelib_osx.c -o bin/equ_schroeder5 -I/usr/local/include -lm

bin/fatchdb: fatchdb.c Filelib_osx.c
	gcc fatchdb.c Filelib_osx.c -o bin/fatchdb -I/usr/local/include -lm

# bin/fft: fft.c Filelib_osx.c
# 	gcc fft.c Filelib_osx.c -o bin/fft -I/usr/local/include -lm

bin/find_cutpoint: find_cutpoint.c Filelib_osx.c
	gcc find_cutpoint.c Filelib_osx.c -o bin/find_cutpoint -I/usr/local/include -lm

bin/henkan: henkan.c Filelib_osx.c
	gcc henkan.c Filelib_osx.c -o bin/henkan -I/usr/local/include -lm

# bin/ifft: ifft.c Filelib_osx.c
# 	gcc ifft.c Filelib_osx.c -o bin/ifft -I/usr/local/include -lm

bin/imp_add: imp_add.c Filelib_osx.c
	gcc imp_add.c Filelib_osx.c -o bin/imp_add -I/usr/local/include -lm

bin/imp_add_by10: imp_add_by10.c Filelib_osx.c
	gcc imp_add_by10.c Filelib_osx.c -o bin/imp_add_by10 -I/usr/local/include -lm

bin/inverse: inverse.c Filelib_osx.c
	gcc inverse.c Filelib_osx.c -o bin/inverse -I/usr/local/include -lm

bin/mono2LR: mono2LR.c Filelib_osx.c
	gcc mono2LR.c Filelib_osx.c -o bin/mono2LR -I/usr/local/include -lm

bin/peaking_filter: peaking_filter.c Filelib_osx.c
	gcc peaking_filter.c Filelib_osx.c -o bin/peaking_filter -I/usr/local/include -lm

bin/print_siglen: print_siglen.c Filelib_osx.c
	gcc print_siglen.c Filelib_osx.c -o bin/print_siglen -I/usr/local/include -lm

bin/random: random.c Filelib_osx.c
	gcc random.c Filelib_osx.c -o bin/random -I/usr/local/include -lm

bin/scaling_max_instant_amp: scaling_max_instant_amp.c Filelib_osx.c
	gcc scaling_max_instant_amp.c Filelib_osx.c -o bin/scaling_max_instant_amp -I/usr/local/include -lm

bin/sepach: sepach.c Filelib_osx.c
	gcc sepach.c Filelib_osx.c -o bin/sepach -I/usr/local/include -lm

bin/sinwave: sinwave.c Filelib_osx.c
	gcc sinwave.c Filelib_osx.c -o bin/sinwave -I/usr/local/include -lm

bin/timeconvo: timeconvo.c Filelib_osx.c
	gcc timeconvo.c Filelib_osx.c -o bin/timeconvo -I/usr/local/include -lm

bin/unbias: unbias.c Filelib_osx.c
	gcc unbias.c Filelib_osx.c -o bin/unbias -I/usr/local/include -lm

bin/zeropad_anyfile: zeropad_anyfile.c Filelib_osx.c
	gcc zeropad_anyfile.c Filelib_osx.c -o bin/zeropad_anyfile -I/usr/local/include -lm


# portaudio

bin/2chplay: 2chplay.c Filelib_osx.c
	gcc 2chplay.c Filelib_osx.c -o bin/2chplay -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/closed_loop_new: closed_loop_new.c Filelib_osx.c
	gcc closed_loop_new.c Filelib_osx.c -o bin/closed_loop_new -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/monoplay: monoplay.c Filelib_osx.c
	gcc monoplay.c Filelib_osx.c -o bin/monoplay -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/monoplay2: monoplay2.c Filelib_osx.c
	gcc monoplay2.c Filelib_osx.c -o bin/monoplay2 -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/monoplay_48k: monoplay_48k.c Filelib_osx.c
	gcc monoplay_48k.c Filelib_osx.c -o bin/monoplay_48k -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/monoplay_8kHz: monoplay_8kHz.c Filelib_osx.c
	gcc monoplay_8kHz.c Filelib_osx.c -o bin/monoplay_8kHz -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/monoplay_alter: monoplay_alter.c Filelib_osx.c
	gcc monoplay_alter.c Filelib_osx.c -o bin/monoplay_alter -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/monorecord: monorecord.c Filelib_osx.c
	gcc monorecord.c Filelib_osx.c -o bin/monorecord -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/playrec_2ch_inPath: playrec_2ch_inPath.c Filelib_osx.c
	gcc playrec_2ch_inPath.c Filelib_osx.c -o bin/playrec_2ch_inPath -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/playrec_2ch_new_kai: playrec_2ch_new_kai.c Filelib_osx.c
	gcc playrec_2ch_new_kai.c Filelib_osx.c -o bin/playrec_2ch_new_kai -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/playrec_mono: playrec_mono.c Filelib_osx.c
	gcc playrec_mono.c Filelib_osx.c -o bin/playrec_mono -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/playrec_mono_inPath: playrec_mono_inPath.c Filelib_osx.c
	gcc playrec_mono_inPath.c Filelib_osx.c -o bin/playrec_mono_inPath -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices

bin/playrec_multi: playrec_multi.c Filelib_osx.c
	gcc playrec_multi.c Filelib_osx.c -o bin/playrec_multi -I/usr/local/include -L/usr/local/Cellar/portaudio/19.6.0/lib -lportaudio -lm -framework CoreAudio -framework AudioToolbox -framework AudioUnit -framework CoreServices


# fftw
bin/fftout2: fftout2.c Filelib_osx.c
	gcc fftout2.c Filelib_osx.c -o bin/fftout2 -I/usr/local/include -L/usr/local/lib -lfftw3 -lm

bin/fftout3: fftout3.c Filelib_osx.c
	gcc fftout3.c Filelib_osx.c -o bin/fftout3 -I/usr/local/include -L/usr/local/lib -lfftw3 -lm

bin/fftout4: fftout4.c Filelib_osx.c
	gcc fftout4.c Filelib_osx.c -o bin/fftout4 -I/usr/local/include -L/usr/local/lib -lfftw3 -lm

bin/make_whitenoise: make_whitenoise.c Filelib_osx.c
	gcc make_whitenoise.c Filelib_osx.c -o bin/make_whitenoise -I/usr/local/include -L/usr/local/lib -lfftw3 -lm

# umasig

# libumasig 
lib/libumasig.a: c_vector.o complex.o conv.o fft.o plot.o random.o speech.o utils.o vector.o window.o
	ar r lib/libumasig.a c_vector.o complex.o conv.o fft.o plot.o random.o speech.o utils.o vector.o window.o

.INTERMEDIATE: c_vector.o complex.o conv.o fft.o plot.o random.o speech.o utils.o vector.o window.o

c_vector.o: umasig/c_vector.c
	gcc -c umasig/c_vector.c -o c_vector.o

complex.o: umasig/complex.c
	gcc -c umasig/complex.c -o complex.o

conv.o: umasig/conv.c
	gcc -c umasig/conv.c -o conv.o

fft.o: umasig/fft.o
	gcc -c umasig/fft.c -o fft.o

plot.o: umasig/plot.o
	gcc -c umasig/plot.c -o plot.o

random.o: umasig/random.o
	gcc -c umasig/random.c -o random.o

speech.o: umasig/speech.o
	gcc -c umasig/speech.c -o speech.o

utils.o: umasig/utils.o
	gcc -c umasig/utils.c -o utils.o

vector.o: umasig/vector.o
	gcc -c umasig/vector.c -o vector.o

window.o: umasig/window.o
	gcc -c umasig/window.c -o window.o

# programs using umasig
bin/calc_ITD: calc_ITD.c Filelib_osx.c lib/libumasig.a
	gcc calc_ITD.c Filelib_osx.c -o bin/calc_ITD -I/usr/local/include -I./umasig -L./lib -lm -lumasig

bin/fff: fff.c Filelib_osx.c lib/libumasig.a
	gcc fff.c Filelib_osx.c -o bin/fff -I/usr/local/include -I./umasig -L./lib -lm -lumasig

bin/linear_inpo_hrir_using_ATD: linear_inpo_hrir_using_ATD.c Filelib_osx.c lib/libumasig.a
	gcc linear_inpo_hrir_using_ATD.c Filelib_osx.c -o bin/linear_inpo_hrir_using_ATD -I/usr/local/include -I./umasig -L./lib -lm -lumasig
