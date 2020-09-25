# Create your tests here.


# def outer(params):
#     def pri(func):
#         def one(*args, **kwargs):
#             return func(args, kwargs)
#         return one
#     return pri
#
#
# @outer('hello')  # test=outer('hello')(test)
# def test(*args, **kwargs):
#     print('------test-method-----')
#     print(args)
#
#
# if __name__ == '__main__':
#
#     test(11, b=5)

# def outer(params):
#     def pri(func):
#         def one(Demo, *args, **kwargs):
#             print(params)
#             return func(Demo, args, kwargs)
#         return one
#     return pri
#
#
# class Demo:
#     @outer('hello')  # test=outer('hello')(test)
#     def test(self, a, b):
#         print('------test-method-----')
#         print(a, b)
#
#
# if __name__ == '__main__':
#     d = Demo()
#     d.test(11, b=121)


def checkLogin(next):
    def inner(func):
        def wrapper(CenterView, request, *args, **kwargs):
            print(next)
            return func(CenterView, request, *args, **kwargs)
            # return redirect(reverse('user:login'))
        return wrapper
    return inner


class GoCartView:
    @checkLogin(123)
    def get(self, request):
        # 创建CartManager对象
        # 查询所有所有购物信息
        print(request)


if __name__ == '__main__':
    g = GoCartView()
    g.get('request = request')