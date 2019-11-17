import Vectors2d as Vc


def str_changer(string):
    string.strip(' ()')
    if string.isalnum() or string.replace('.', '').isalnum():
        if string.isdigit():
            string = int(string)
            component = None
            return string, component
        if '.' in string:
            try:
                string = float(string)
                component = None
                return string, component
            except ValueError:
                pass

        if string[-1] in 'iIxXîÎ':
            string = string.rstrip('iIxXîÎ')
            string, component = str_changer(string)
            component = 'x'
            return string, component
        elif string[-1] in 'jJyYĵĴ':
            string = string.rstrip('jJyYĵĴ')
            string, component = str_changer(string)
            component = 'y'
            return string, component
    if (',' in string) or (' ' in string) or ('+' in string):
        if ',' in string:
            string = string.split(',')
        elif '+' in string:
            string = string.split('+')
        else:
            string = string.split()
        if len(string) == 2:
            string[0], temp_cx = str_changer(string[0])
            string[1], temp_cy = str_changer(string[1])
            if temp_cx == 'y' or temp_cy == 'x':
                string[0], string[1] = string[1], string[0]
            string = [float(i) for i in string]
            component = 'xy'
            return string, component


def operand_optimize(func):
    def common(self, obj):

        result = []
        if isinstance(obj, Vc.Vector2d):
            result = [obj.val['X'], obj.val['Y']]
        elif isinstance(obj, tuple) or isinstance(obj, list):
            if len(obj) == 2:
                for i in obj:
                    if isinstance(i,int) or isinstance(i,float) or isinstance(i,complex):
                        result.append(i)
                    elif i.isinstance(str):
                        temp_obj, component = str_changer(i)
                        if component is None:
                            result.append(temp_obj)
                        elif component == 'x':
                            result = [temp_obj] + result
                        elif component == 'y':
                            result = result + [temp_obj]
        elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
            result = [obj, obj]
        elif isinstance(obj, str):
            temp_obj, component = str_changer(obj)
            if component == 'xy':
                result = temp_obj.copy()
        return func(self, result)

    return common


