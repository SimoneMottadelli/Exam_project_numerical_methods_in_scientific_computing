
def main():
    file1 = open("../results/1output_1000_step_10.txt", "r")
    file2 = open("../results/2output_1000_step_10.txt", "r")
    file3 = open("../results/3output_1000_step_10.txt", "r")
    file4 = open("../results/4output_1000_step_10.txt", "r")

    for line in file1:
        print(line)


if __name__ == '__main__':
    main()