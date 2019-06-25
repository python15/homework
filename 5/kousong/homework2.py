#fifth week2
d={}
while True:
    n=int(input('give me a number'))
    def cache(fn):
        def _logger(n):
            
            dic=d.keys()
            if n in dic:
                return (d[n])
            else:
            
                d[n] = fn(n)
                return (d[n])       
        return _logger
    @cache
    def fib(n):
        if n<3:
            return (n)
        return(fib(n-2)+fib(n-1))
    print(fib(n))