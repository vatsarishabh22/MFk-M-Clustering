if __name__ == '__main__':
    input_file_path = "filepath/Data.csv" #address of input file
    columns = 30     #no of columns in the csv file (I kept 30 as value)
​
    field_to_value_to_count = dict()
    with open(input_file_path, "r") as in_f:
        count = 0
        for line in in_f:
            count += 1
            if count == 1:
                continue
            fields_values = line.split(",")
​           
            for i in range(columns):
                if i not in field_to_value_to_count:
                    field_to_value_to_count[i] = dict()
                if fields_values[i] not in field_to_value_to_count[i]:
                    field_to_value_to_count[i][fields_values[i]] = 0
                field_to_value_to_count[i][fields_values[i]] += 1
    print("Total records: " + str(count))
​
    with open(input_file_path, "r") as in_f:
        output_file_path = "filepath/transformed_Data.csv"
        with open(output_file_path, "w") as out_f:
            count = 0
            for line in in_f:
                count += 1
                if count == 1:
                    out_f.write(line.strip() + "\n")
                    continue
                fields_values = line.split(",")
​
                for i in range(columns-1):                         # removing non categorical column
                    field_value = fields_values[i]
                    freq = field_to_value_to_count[i][field_value]
                    relative_freq = float(freq) / 10000
                    out_f.write(str(relative_freq) + ",")
                field_value = fields_values[29]
                freq = field_to_value_to_count[29][field_value]
                relative_freq = float(freq) / 10000
                out_f.write(str(relative_freq) + "\n")
