from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------




if __name__ == "__main__":
    import string

    alphabet = string.ascii_lowercase
    password_found = False

    for ch1 in alphabet:
        if password_found:
            break
        for ch2 in alphabet:
            if unzip_with_7z(zip_file_path, dest_path, ch1 + ch2 + secret_password):
                password_found = True
                break

