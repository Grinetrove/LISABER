import camera as c
import time as t






    




def timeout_test(file_path = "PythonScripts/Scripts/Graham/Test_Logs/timeoutlog.txt",count_per_test = 25, time_between_tests = 1):
    # if str(input(f"This will write over {file_path}. Do you wish to continue? (y/n)")).lower != 'y':
    #     quit()
    with open(file_path, "a") as file1:
                file1.write(f"\nRunning Test {t.ctime()} - {count_per_test} photo(s) per test - {time_between_tests} second(s) inbetween\n\n")
                file1.close
    camera = c.EasyCamera("My Camera")
    for timeout in reversed(range(50,1250,50)):
        camera.issues = 0
        camera.clear_folder()
        camera.take_photos(count=count_per_test, time_between=time_between_tests, delay = 0,timeout = timeout)
        with open(file_path, "a") as file1:
            file1.write(f"With a timeout of {timeout}ms : The camera failed to capture\t{(camera.issues/count_per_test)*100}% of the time\n")
            file1.close


timeout_test() 





