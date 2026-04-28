class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = str(num)
        divided_number = []
        def check_digit(num):
            length = len(num)
            i = 0
            while length > 0 and i < length :
                if length == 4 :
                    divided_number.append(int(num[i])* 1000)
                    i+=1
                    divided_number.append(int(num[i])* 100)
                    i+= 1
                    divided_number.append(int(num[i])* 10)
                    i+=1
                    divided_number.append(int(num[i])*1)
                    i+=1

                elif length == 3 :
                    divided_number.append(int(num[i])* 100)
                    i+= 1
                    divided_number.append(int(num[i])* 10)
                    i+=1
                    divided_number.append(int(num[i])*1)
                    i+=1  
                
                elif length == 2 :
                    divided_number.append(int(num[i])* 10)
                    i+=1
                    divided_number.append(int(num[i])*1)
                    i+=1

                else :
                    divided_number.append(int(num[i])*1)
                    i+=1
            return divided_number
        
        digits = check_digit(num) 

        map = {
            3000: 'MMM',
            2000: 'MM',
            1000: 'M',
            900: 'CM',
            800: 'DCCC',
            700: 'DCC',
            600: 'DC',
            500: 'D',
            400: 'CD',
            300: 'CCC',
            200: 'CC',
            100: 'C',
            90: 'XC',
            80: 'LXXX',
            70: 'LXX',
            60: 'LX',
            50: 'L',
            40: 'XL',
            30: 'XXX',
            20: 'XX',
            10: 'X',
            9: 'IX',
            8: 'VIII',
            7: 'VII',
            6: 'VI',
            5: 'V',
            4: 'IV',
            3: 'III',
            2: 'II',
            1: 'I'
        }

        roman = ""
        for num in digits :
            if num in map :
                roman = roman + map[num]

        return roman  

        

            
            

          

p = Solution()
print(p.intToRoman(1994))