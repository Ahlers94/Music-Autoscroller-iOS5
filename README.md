# Music-Autoscroller-iOS5

## PURPOSE

This is an HTML app designed for musicians to autoscroll .txt files on the original iPad running iOS 5.1.1 

## WHY WOULD ANYONE USE AND IPAD 1?

- If you are a DIY type this will save you hundreds or thousands of dollars in the long run on expensive hardware/subscriptions.

- An original iPad is basically e-waste at this point, but you can recycle it into something usable

- and not worry too much about getting lost/damaged/stolen.

- It has a fairly large screen (7.75 × 5.82 inches) but small enough to fit in a tablet holder or in a bag.

- Great battery life, recommend replacing the battery

## ARCHITECTURE

To circumvent the lack of a File System Access API in iOS 5, 
this app utilizes a Client-Server model over a local network. 
By leveraging GoodReader’s WiFi server as a backend, 
the HTML app (running in iCabMobile) can perform asynchronous fetches for .txt assets and manifest data.

Data Persistence: Setlists and History logs are handled via HTTP POST requests to the local GoodReader server, 
ensuring data persists across sessions despite the browser’s limited local storage.
LocalStorage is used instead of Cookies for persistence on a per song basis of:
- autoscroll speed
- scroll position
- zoom level
so if you have dialed in the desired scroll speed during practice it will be recalled on stage.

## HARDWARE/SOFTWARE REQUIREMENTS

- iPad 1st Generation

- iOS 5.1.1 (Jailbroken)

- GoodReader (found on Archive.org)

- iCabMobile browser (found on Archive.org)

## WHY DO WE NEED ALL OF THIS SOFTWARE?

- It requires a Jailbroken iPad on iOS 5.1.1 with Backgrounder downloaded from Cydia, 
GoodReader set up as a WiFi server, and iCabMobile as the browser.

- Backgrounder is able to run two apps simultaneously. First run Backgrounder, then open GoodReader,
start the WiFi server, and finally open iCabMobile. 

- GoodReader is necessary as a WiFi server because iOS5 doesn't have a File System Access API.

- iCabMobile was better than Safari for a fullscreen mode back then. 

- The UI is designed around the buttons in iCabMobile's fullscreen mode.

## OPEN A SONG

- On the top bar there are controls to open a song, which can be pressed to open a cached list from the server,

- or you can hold it down for a second to refresh the list from the server.

## SETLISTS

- Pressing the button with 3 bars at the top has the same effect as swiping right, which will bring up the setlists menu.

- At the bottom of the setlists menu you can add the song you're currently viewing to the list, save the current setlist,
or view available setlists.  Setlists are stored as .txt files on the Wifi Server under /My Documents/Setlists

## HISTORY

- There are two tabs at the top of the setlists menu, the other tab is history.

- Press the history button and it will show the date and time every file was accessed.

- Helpful if you want to know what you played and when.

## TRANSPOSE

- Press the - and + buttons to transpose the key up or down 12 semitones.  The rst button next to it will reset it back to 0.

## SONG TITLE

-  Displayed on the top bar, this is the current song loaded.

## PLAY/STOP

- At the bottom bar the Play/Stop buttons will start autoscroll and stop autoscrolling.

## PREV/NEXT

- This navigates through your current setlist in order.

## FONT SIZE

- Pinch to zoom or adjust the text size by pressing the A- and A+ buttons on the bottom bar.

## AUTOSCROLL SPEED

- 20 speeds available, press up and down arrows to change the speed.  The speed you chose will be remembered for each song.


