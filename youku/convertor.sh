## the file convert all the flv files in the cwd to mp3 files
function generate_wav
{
    for file in $(ls)
    do
        echo $file
        ffmpeg -i $file $file".wav" 2>/dev/null
    done
}

function generate_mp3
{
    for file in $(ls *.wav)
    do
        echo $file
        lame $file $file".mp3"
    done
}

function rename_mp3
{
    for file in $(ls *.mp3)
    do
        short_filename=$(echo $file|awk -F"." '{print $1}')        
        mv $file $short_filename".mp3"
    done

}

function cleanup
{
    rm *.wav*
    mkdir outputmp3
    mv *.mp3 outputmp3
}

generate_wav
generate_mp3
rename_mp3
cleanup`


