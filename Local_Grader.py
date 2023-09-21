import os
import subprocess
import filecmp
import re
from enum import Enum


class Mode(Enum):
    exe = 1
    txt = 2


class Output(Enum):
    none = 0
    TF = 1
    long = 2


# TODO: modify test configurations
class Config:
    def __init__(self, mode=Mode.exe, output=Output.TF, test_file_suffix='.as', test_output_suffix='',
                 example_file_suffix='.txt', pre_execute_commands=[], exe_compile_command='', exe_run_command='',
                 exe_name='assembler', example_compile_command='', example_run_command='', example_name=''):
        self.mode = Mode.exe
        self.output = Output.TF
        self.test_file_suffix = '.as'
        self.test_output_suffix = '.txt'
        self.example_file_suffix = '.txt'
        self.pre_execute_commands = []
        self.exe_compile_command = 'gcc -std=c99 -Wall -Werror -o3 assembler.c -o assembler -lm'
        self.exe_name = ''
        self.example_compile_command = ''
        self.example_name = ''


if __name__ == '__main__':
    # TODO: modify the fields of configure
    configure = Config(mode=Mode.exe,
                       output=Output.TF,
                       test_file_suffix='.as',
                       test_output_suffix='.txt',
                       example_file_suffix='.txt',
                       pre_execute_commands=['gcc -std=c99 -Wall -Werror -o3 assembler.c -o assembler -lm'],
                       exe_compile_command='gcc -std=c99 -Wall -Werror -o3 simulator.c -o simulator -lm',
                       exe_run_command='',
                       exe_name='assembler',
                       example_compile_command='gcc -std=c99 -Wall -Werror -o3 zsimulator.c -o zsimulator -lm',
                       example_run_command='',
                       example_name='zsimulator')
    test_file_pattern = 'test-\w+' + configure.test_file_suffix

    if len(configure.pre_execute_commands) != 0:
        for command in configure.pre_execute_commands:
            os.system(command)

    # find test files
    current_path = os.getcwd()
    files = os.listdir(current_path)
    test_files = []
    for file in files:
        if re.match(test_file_pattern, file, flags=0) is not None:
            name = file[5:len(file) - len(configure.test_file_suffix)]
            test_files.append(name)
    print(test_files)

    os.system(configure.exe_compile_command)
    if configure.mode == Mode.exe:
        os.system(configure.example_compile_command)

    for test in test_files:
        # run test files
        assemble = './assembler mult.as mult.mc'
        mult = './zsimulator mult.mc > m.txt'
        os.system(assemble)
        os.system(mult)
        if configure.output == Output.TF:
            # diff the results
            ans_file = 'test_' + test + '_ans.txt'  # test_add_ans.txt
            correct_file = 'z_' + test + '_ans.txt'
            diff_result = filecmp.cmp(ans_file, correct_file, shallow=False)
            print(test, end=': \t')
            print(diff_result)

