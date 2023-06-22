# AutoGPG
# Python Script: GPG Key Importer and File Encryptor

This Python script automates the process of importing GPG keys and encrypting files using those keys. It provides options to import keys from the local machine or the Ubuntu key server, and then encrypt files based on the selected key.

## Executable Version: AutoGPG

If you prefer not to install the prerequisites manually, an executable version of the script called "AutoGPG.exe" is available. AutoGPG bundles all the necessary dependencies, allowing you to run the script without installing additional packages, but it runs a little slow ans you still have to install # gnupg on your system.

### Download AutoGPG

You can download the AutoGPG executable from the following link:

[AutoGPG Download](https://github.com/OMARomd23/AutoGPG/releases)

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:

- Python 3.x
- GnuPG (GPG) command-line tool (`gpg`)
- Playwright Python library
- Colorama Python library


You can install the required Python packages by running the following command:

```bash
pip install playwright colorama
```
then

```bash
playwright install
```

You also need to have the GnuPG command-line tool (`gpg`) installed on your machine. If it's not already installed, you can install it on Ubuntu using the following command:

```bash
sudo apt-get install gnupg
```
In Windows 

```powershell
winget install gnupg
```
## Usage

To use the script, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.

2. Run the Python script `autogpg.py` using the following command:

   ```bash
   python autogpg.py
   ```

3. The script will display a menu with two options:

   ```
   What do you want to do:
   1: To import a key
   2: To encrypt using a key that is already imported
   ```

4. Choose an option by entering the corresponding number and pressing Enter.

   - If you choose option 1, you will be prompted to select the source of the key: the local machine or the Ubuntu key server.

     - If you choose the local machine, you need to provide the path to the directory containing the public key files you want to import.

     - If you choose the Ubuntu key server, you will be prompted to enter the key name and the path to save the key file.

   - If you choose option 2, you will be prompted to enter the path to the files you want to encrypt and the recipient's username.

5. Follow the on-screen instructions and provide the required information as prompted.

6. The script will perform the selected action (importing keys or encrypting files) and display the progress.

7. If you choose to encrypt files and confirm moving the encrypted files to another location, you will be prompted to enter the destination folder.

8. Once the script finishes executing, you can check the results based on the action you performed.


## License

This script is licensed under the [MIT License](LICENSE).

## Disclaimer

- This script is provided as-is and without warranty.

## Contact

If you have any questions or need further assistance, feel free to contact the author:

  - Name: omar
- Email: omsoudomar23@gmail.com
