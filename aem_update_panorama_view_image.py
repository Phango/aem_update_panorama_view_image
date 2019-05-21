#!/usr/bin/python
import os
import subprocess

def main():
    path_to_original_zip_file = ''
    path_to_krpano_folder = ''

    while not os.path.exists(path_to_original_zip_file): 
      path_to_original_zip_file = raw_input('Please specify path to the zipped file downloaded from AEM: ')
      print('Zipped file path: ' + path_to_original_zip_file)

      output_path = path_to_original_zip_file.rsplit('/', 1)[0]
      zip_file_name = str(path_to_original_zip_file.rsplit('/', 1)[1]).split('.')
      unzipped_file_path = output_path + '/' + zip_file_name[0]
      new_zip_file_name = '_updated.'.join(zip_file_name)

    while not os.path.exists(path_to_krpano_folder): 
      path_to_krpano_folder = raw_input('Please specify path to krpano output folder: ')
      print('krpano output folder file path: ' + path_to_krpano_folder)

    print('Zipping file to: ' + output_path)
    print('Output zip file name: ' + new_zip_file_name)
    subprocess.call(['unzip', path_to_original_zip_file, '-d', output_path])

    print('Moving krpano files: ' + path_to_krpano_folder)
    # FIXME: update panorama_files_path_in_zip_file according to what it needs to be 
    panorama_files_path_in_zip_file = '/original/jcr_root/destination_for_new_stuff/' 
    target_path = output_path + panorama_files_path_in_zip_file
    print('Copying file from: ' + path_to_krpano_folder + ' to ' + target_path)
    subprocess.call(['cp', '-R', path_to_krpano_folder, target_path])

    print('Zipping updated file as: ' + new_zip_file_name)
    subprocess.call(['zip', '-r', new_zip_file_name, unzipped_file_path + '/jcr_root/', unzipped_file_path + '/META-INF/', '-x', '*.DS_Store'])

# clean up __MACOSX file if there is one

if __name__ == "__main__":
    # execute only if run as a script
    main()