# Music-Autoscroller-iOS5

## PURPOSE

This is an HTML app designed for musicians to autoscroll .txt files on the original iPad running iOS 5.1.1 

## ARCHITECTURE

To circumvent the lack of a File System Access API in iOS 5, 
this app utilizes a Client-Server model over a local network. 
By leveraging GoodReader’s WiFi server as a backend, 
the HTML app (running in iCabMobile) can perform asynchronous fetches for .txt assets and manifest data.

Data Persistence: Setlists and History logs are handled via HTTP POST requests to the local GoodReader server, 
ensuring data persists across sessions despite the browser’s limited local storage.
LocalStorage is used instead of Cookies for persistance on a per song basis of 
autoscroll speed
scroll position
zoom level


## HARDWARE/SOFTWARE REQUIREMENTS

iPad 1st Generation

iOS 5.1.1 (Jailbroken)

GoodReader (found on Archive.org)

iCabMobile browser (found on Archive.org)

## WHY DO WE NEED ALL OF THIS?

It requires a Jailbroken iPad on iOS 5.1.1 with Backgrounder downloaded from Cydia, 
GoodReader set up as a WiFi server, and iCabMobile as the browser.

Backgrounder is able to run two apps simultaneously. First run Backgrounder, then open GoodReader,
start the Wifi server, and finally open iCabMobile. 

GoodReader is necessary as a WiFi server because iOS5 doesn't have a File System Access API.
iCabMobile was better than Safari for a fullscreen mode back then. 
The UI is designed around the buttons in fullscreen.

## OPEN A SONG

On the top bar there are controls to open a song, which can be pressed to open a cached list from the server,
or you can hold it down for a second to refresh the list from the server.

## SETLISTS

Pressing the button with 3 bars at the top has the same effect as swiping right, which will bring up the setlists menu.

At the bottom of the setlists menu you can add the song you're currently viewing to the list, save the current setlist,
or view available setlists.  Setlists are stored as .txt files on the Wifi Server under /My Documents/Setlists

## HISTORY

There are two tabs at the top of the setlists menu, the other tab is history. This will show the date and time every file was accessed.
Helpful if you want to know what you played and when.

## TRANSPOSE

You can press the - and + buttons to transpose the key up or down 12 semitones.  The rst button next to it will reset it back to 0.

## SONG TITLE will be displayed on the top bar, this is the current song loaded.

## PLAY/STOP

At the bottom bar the Play/Stop buttons will start autoscroll and stop autoscrolling.

## PREV/NEXT

This navigates through your current setlist in order.

## FONT SIZE

You can pinch to zoom or adjust the text size by pressing the A- and A+ buttons on the bottom bar.

## AUTOSCROLL SPEED

There are 20 speeds available and you can press up and down arrows to change the speed.


