from typing import Optional, Dict


class BaseTag:

    def __init__(self, xpath: str = '//*', **kwargs):
        self.user_input = kwargs
        self.xpath = xpath
    
    @property
    def xpath(self) -> str:
        """
        Get the xpath value as a string.
        """
        return self._xpath

    @xpath.setter
    def xpath(self, xpath: str) -> str:
        """
        Set the xpath value of the string as value
        """
        if not isinstance(xpath, str):
            raise ValueError('xpath must be of type str')

        for key in self.user_input.keys():
            if key.startswith('html_'):
                new_value = key[5:]
                xpath += f'[@{new_value}={self.user_input[key]}]'
            else:
                xpath += f'[@{key}={self.user_input[key]}]'
        self._xpath = xpath

    def __repr__(self):
        return f'{self.__class__.__name__}({str(self.xpath)})'



if __name__ == '__main__':
    def get_tags():
        a = BaseTag('//br', html_class='new_class', html_id="old_id", time_attr="newtest")
        print('__repr__: ', a)
        print('a.xpath: ', a.xpath)
        print('a: ', a)
        b = BaseTag()
        print(b)
            
    get_tags()