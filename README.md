# SpotiToYt

SpotiToYt is a Python application that tracks users spotify activity and creates youtube playlist based on your current activity. The application uses the Spotify API and YouTube Data API to search for songs on YouTube and create playlists.

## Resources used
- Spotipy
- Pytube
- Google Auth OAuthlib
- Google API Python Client

## Features

- Create a YouTube playlist based on a Spotify playlist
- Search for songs on YouTube using Spotify track information
- Add songs to the created YouTube playlist

## Before you install

Before you can use SpotiToYt, you need to create a Spotify Developer application and a Google Developer application to get your `client_id`, `client_secret`, and `redirect_uri` for Spotify, and `client_secret.json` for YouTube. Here's how you can do it:

### Spotify Developer Application

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on 'Create an App'.
4. Fill in the 'Name', 'Description', and redirect_uri (I recommend using http://localhost:3000/) for your new app, then click 'Create'.
5. On the next page, you will see your `client_id` and `client_secret`. You will need these to authenticate your application.
6. Click on 'Edit Settings'.
7. In the 'Redirect URIs' field, enter the URI where you want Spotify to redirect you after a successful login.
8. Click 'Save'.

### Google Developer Application

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Navigate to the "OAuth consent screen" and configure it.
4. Go to "Credentials" and create an OAuth 2.0 Client ID.
5. Download the `.json` file and rename it to `client_secret.json`

## Installation

1. **Ensure Python 3.9 or later is installed**:
   - If not, download it from the [official website](https://www.python.org/downloads/).
   - Make sure to add Python to PATH during installation.

2. **Clone the repository**:
   - If you don't have Git installed, download it from the [Git Official Website](https://git-scm.com/download/win).

   To clone the repository, follow these steps:

   - Create a new folder where you want to clone the repository.
   - Right-click on the folder and select "Open in Terminal" to open a terminal window.
   - In the terminal window, run the following command to clone the repository:

      ```sh
      git clone https://github.com/PanPeryskop/SpotiToYt
      ```

   This will download all the files and folders from the repository to your local machine.

3. **Open the SpotiToYt folder**.

4. **Run the 'setup.bat' to install required packages**.

## Usage

1. Open the folder in cmd and type `python.exe spoti-to-yt.py` or open the [`run.bat`] file in the SpotiToYt folder (If it doesn't work, modify the bat file in notepad and change `python.exe` to the direct path to your `python.exe`). The [`run.bat`]file also checks for updates and automatically updates the program if a new version is available.

2. The application will ask you to enter your `client_id`, `client_secret`, and `redirect_uri` for Spotify, and it will use the [`client_secret.json`] for YouTube.

3. The application will then create a YouTube playlist based on your Spotify activity.

Enjoy your music on YouTube!
