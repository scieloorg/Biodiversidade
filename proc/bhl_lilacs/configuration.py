import os
class Configuration:
    def __init__(self, filename = 'configuration.ini'):
        f = open(filename, 'r')
        self.config = {}
        for c in f.readlines():
            if '=' in c:
                c = c.strip('\n').split('=')
                self.config[c[0]] = c[1].replace('\\', '/')
                if '_PATH' in c[0] and '/' in self.config[c[0]]:
                    if not os.path.exists(self.config[c[0]]):
                        os.makedirs(self.config[c[0]])
        f.close()

    def check_parameters(self, config_parameters):
        error = False
        for i in config_parameters:
            if i in self.config.keys():
                if len(self.config[i]) == 0:
                    print('No value for ' + i)
            else:
                print('Missing ' + i)
                error = True
                break
        return (not error)

    def return_parameters(self, config_parameters):
        r = []
        for param in config_parameters:
            r.append(self.config[param])
            
        return r
