import os
import subprocess

if __name__ == '__main__':

    test_names = {'nor'}
    run_diff = False

    for name in test_names:
        # get .as file
        run = './assembler test_' + name + '.as test_' + name + '.mc'
        # get answer
        spec = './simulator test_' + name + '.mc > ' + name + '_ans.txt'
        os.system(run)
        os.system(spec)
        subprocess.run(spec, capture_output=True)
        # get correct answer
        if run_diff:
            # diff the results
            diff = 'diff ' + name + '_ans.txt ' + 'name.correct'
            subprocess.run(diff, capture_output=True)
        # subprocess.check_output()



    
