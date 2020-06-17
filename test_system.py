import os
import pathlib

def run_system_tests():
    """
    This function runs all the tests in the system_tests folder to test that the system is working
    :return: Does not return anything, but should have no errors if everything passes
    """
    system_path = pathlib.Path().absolute() #The path to the current folder

    path_to_tests = pathlib.Path().joinpath(system_path,"system_tests") #This string will hold the path to the tests we will run


    # Now that we have the path, we want to run all the files in that path
    test_files = os.listdir(path_to_tests)  # Get all test files

    for test_file in test_files:
        if test_file.endswith('.py'): #Python test
            test_file_path = pathlib.Path().joinpath(path_to_tests,test_file) #Get total path

            os.system("pytest " + str(test_file_path)) #Run the pytest file

#C:\Users\Vishn\Downloads\anomaly-explain\system_tests\test_rules.py
if __name__ == '__main__':
        run_system_tests()