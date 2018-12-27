CHECKPOINT_DIR="/Users/ronggong/Documents_using/pianoAI/data/transcription_models/onset_and_frames"

mp3_array=()
for dir in /Users/ronggong/Documents_using/pianoAI/data/测试数据mp3+midi/*
do
    if [[ -d $dir ]]; then
        for file in $dir/*
        do
            if [[ -f $file ]] && [[ $file == *.mp3 ]]; then
                mp3_array+=($file)
            fi
        done
    fi
done

# printf '%s\n' "${mp3_array[@]}"

onsets_frames_transcription_transcribe --acoustic_run_dir="${CHECKPOINT_DIR}" ${mp3_array[@]}