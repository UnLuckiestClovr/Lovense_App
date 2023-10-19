# Lovense_App
Attempting to make a GUI ran application that interacts with and controls Lovense Toys based in their current model and functions using an API setup.


Goals:
    Make a Locally run Python executable Application implementing easy-to-use GUI.
    Use an automatic persistence setting that locally saves data onto your PC without the need to worry about re-applying setting changes over time.

_________________________________________________________________________________________________________________________________________________________________________________________________________________

Current Games:
    
    Surprise!
        ~ You input a Value you want as a time interval, 
        it counts that many seconds between each activation then runs a random number between 1 through 10.
            + On a 5 = an activation of 10 to 50% power for 2 to 8 seconds.
            + On a 10 = an activation of 50 to 100% power for 2 to 8 seconds.

_________________________________________________________________________________________________________________________________________________________________________________________________________________


Known Issues:
    1 ~ PyInstaller, which is used to allow Users to read Python code without an Interpreter uses a couple file script named "Win32/Wacatac.C" and "Bearfoos.A" to do this.


Solutions:
    1 ~ Currently no found solutions at this time. Manual Admin fixes include allowing the files through your Window's Defender Wall. Possible Solution includes paying for a Code Signing Certificate to bypass AntiVirus Reads.
