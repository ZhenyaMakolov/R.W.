class FilesProcessor:
    def __init__(self, files_names_list):
        self.files_names_list = files_names_list

    def create_files_dict(self):
        
        files_dict = {}
        
        for file in self.files_names_list:
            with open(file, encoding='utf-8') as file_in_the_process:
                strings_quantity = len(file_in_the_process.readlines())
            with open(file, encoding='utf-8') as file_in_the_process:   
                content = file_in_the_process.read()

            files_dict[file] = [strings_quantity, content]
        
        return files_dict
    
    def str_qw_sorted(self):
        
        str_qw_list = []
        
        for value in list(self.create_files_dict().values()):
            str_qw_list.append(value[0])
        
        return sorted(str_qw_list)

    def write_in_order(self):
        for str_qw in self.str_qw_sorted():
            for key, value in self.create_files_dict().items():
                if str_qw in value:
                    with open('res.txt', 'a') as file:
                        file.write(key + '\n')
                        file.write(str(value[0]) + '\n')
                        file.write(value[1] + '\n')
        

processor = FilesProcessor(['1.txt', '2.txt', '3.txt'])
processor.write_in_order()
        