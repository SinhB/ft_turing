# 42 - ft_turing

Collaborator: [Lou](https://github.com/LouCHANCRIN)

# About:

The goal of this project is to write a program able to simulate a single headed and single tape Turing machine from a json machine description given as parameter.

We choose python as a programing language to write this program.

We also had to write 5 differents machine description in a json format:
- A machine able to compute an `unary addition`
- A machine able to decide whether its input is a `palindrome` or not
- A machine able to decide if the input is a word of the language `0n1n`
- A machine able to decide if the input is a word of the language `02n`
- A machine able to run the first machine of this list (the one computing an unary addition)

For the last one and after several research, we found out that this machine is a `Universal Turing Machine` (UTM) : [Universal Turing Machine Wiki](https://en.wikipedia.org/wiki/Universal_Turing_machine)
Our UTM was built with the help of this [paper](http://people.cs.uchicago.edu/~simon/OLD/COURSES/CS311/UTM.pdf)

For more informations about the subject: [subject](en.subject.pdf)

# Installation

`pip install -r requirements.txt`


# Run

## Machine 0-3:

`python src/ft_turing.py machines_json/<machine_name> <input>`

## Universal Turing Machine:

Encode the choosing machine:

`python src/encode_utm.py machines_json/<machine_name> <input>`

e.g.:
```
~ python src/encode_utm.py machines_json/unary_add.json 11+1                                                                                                                                                    
X0000000000QY1011010110111001011101101101110011011011011011100110101110101001110110111101010011110110111110110111000Z11011011101101
```

This will print the encoded selected machine and create a `utm_encoding_keys.json` for later decoding.

Copy the encoding machine string and run the utm machine as follow:

`python src/ft_turing.py --universal machines_json/universal_turing_machine.json <encoded machine>`

e.g.:
```
~ python src/ft_turing.py --universal machines_json/universal_turing_machine.json X0000000000QY1011010110111001011101101101110011011011011011100110101110101001110110111101010011110110111110110111000Z11011011101101
```

To decode the output, copy the string after the last `0000`, remplace `Z` by one `0` then run the following command:

`python src/decode_utm.py utm_encoding_keys.json <encoded_output>`

E.G. :

```
Last line of the output: 
`[X1111101000Q01011010110111001011101101101110011011011011011100110101110101001110110111101010011110110111110110111000011011011Z1010..]  |  (check_for_end, 0) -> (HALT, 0, RIGHT)`

~ python src/decode_utm.py utm_encoding_keys.json 1101101101010
111..
```
