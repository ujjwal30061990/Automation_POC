*** Settings ***
Library    config.py
Library    timestamp.py

*** Test Cases ***
Open Teraterm
    config.Teraterm
    config.Aampcli
StreamPlaybackVerification
    timestamp.streamplayback
StreamFailureVerification
    timestamp.ExtractTimeStampsstreamfailure
SeekFWplay
    config.seekFW
SeekFWVerification
    timestamp.ExtractTimeStampsSeekFW
SeekRWplay
    config.seekRW
SeekRWVerification
    timestamp.ExtractTimeStampsSeekRW
Pause
    config.pause
PauseVerifiaction
    timestamp.ExtractTimeStampspause
Play
    config.play
PlayVerifiaction
    timestamp.ExtractTimeStampsplay
SchedulePause
    config.schedule_pause_verification
SchedulePauseVerification
    timestamp.ExtractTimeStampsScheduledPause
Play_once
    config.play
SlowMotion
    config.slow_motion
SlowMotionVerification
    timestamp.ExtractTimeStampsSlow
Play_twice
    config.play
StopStream
    config.Stop
StopVerification
    timestamp.ExtractTimeStampsSTOP

StreamPlay
    config.Stream_Play