class StringCalculator:

    def add(self, string):
        if not string:
            return 0

        list_string = self._parse_text(string)
        list_num = self._string_to_num(list_string)
        total = sum(list_num)
        
        return total

    def _parse_text(self, string):
        delimiters = [","]

        has_custom_delimiter = string.startswith("//")
        if has_custom_delimiter:
            string, delimiters = self._extract_delimiter(string)

        string = string.replace("\n", delimiters[0])
        for deli in delimiters:
            string = string.replace(deli, delimiters[0])
        
        list_string = string.split(delimiters[0])

        return list_string
    
    def _extract_delimiter(self, string):
        ind = string.find("\n")
        delimiter_string = string[2:ind]
        string = string[ind+1:]
        
        if "[" not in delimiter_string and "]" not in delimiter_string:
            return string, [delimiter_string]

        delimiters = []
        delimiter = ""
        for char in delimiter_string:
            if char == "]":
                delimiters.append(delimiter)
                delimiter = ""
            elif char != "[":
                delimiter += char
        
        return string, delimiters

    
    def _string_to_num(self, list_string):
        
        list_num = [int(i) for i in list_string]
        neg = []
        for i in range(len(list_num)):
            if list_num[i] < 0:
                neg.append(list_num[i])
                list_num[i] = 0
            if list_num[i] > 1000:
                list_num[i] = 0

        if neg:
            error_msg = ",".join(list(map(str, neg)))
            raise ValueError(f"negatives not allowed: {error_msg}")
        
        return list_num
    




            
