
# URL Shortening with Flask

The aim of this project is to provide a basic application for flask. Included in this project is a way to port forward the server to be access from any network connected to the internet.


## Features

- URL Shortening
- Port reusing (Prevents port from being locked even when application is closed)
- Publicly accessing the app from anywhere in the world.


## Python Dependencies

```bash
  pip install flask
```
    
## Setting up localXposed
1. Sign up for free to [localXposed](https://localxpose.io/?via=meezaan).
2. Head over to localXposed [download link](https://localxpose.io/docs?via=meezaan#download). Download and install the executable for your operating system.
3. Finally, you need to get your access token [here](https://localxpose.io/dashboard/access).


## Forward Porting
1. Depending on your platform run one of the following commands:
```bash
loclx account login # For Linux
```
```bash
loclx.exe account login # For Windows
```
2. Finally, run the following to forward port your web app, however don't forget to change your port number.
```bash
loclx tunnel http --to localhost:5000
```
Once you run this you should see your external link. Mine is "99z9fh46no.loclx.io".
