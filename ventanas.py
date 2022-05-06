
class Ventana:
    __titulo = ''
    __x_sup_izq = 0
    __y_sup_izq = 0
    __x_inf_der = 0
    __y_inf_der = 0
    def __init__(self,t, x_s=0, y_s=0, x_i=500, y_i=500):
        self.__titulo = t
        self.__x_sup_izq = x_s
        self.__y_sup_izq = y_s
        self.__x_inf_der = x_i
        self.__y_inf_der = y_i
    def __str__(self):
        return "titulo:{}  x_sup_izq: {},  y_sup_izq:{},  x_inf_der:{}, y_inf_der:{}".format(self.__titulo, self.__x_sup_izq, self.__y_sup_izq, self.__x_inf_der, self.__y_inf_der)
    def mostrar(self):
        print("titulo:{}  x_sup_izq: {},  y_sup_izq:{},  x_inf_der:{}, y_inf_der:{}".format(self.__titulo, self.__x_sup_izq, self.__y_sup_izq, self.__x_inf_der, self.__y_inf_der))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__y_inf_der - self.__y_sup_izq)
    def ancho(self):
        return(self.__x_inf_der - self.__x_sup_izq)
    def moverDerecha(self,c):
        if self.__x_inf_der < 500:
            self.__x_inf_der += c
        self.__x_sup_izq += c
    def moverIzquierda(self,z):
        if self.__x_sup_izq > 0:
            self.__x_sup_izq -= z
        self.__x_inf_der -= z
    def bajar(self,b=1):
        if self.__y_inf_der < 500:
            self.__y_inf_der +=b
        self.__y_sup_izq += b
    def subir(self,s=1):
        if self.__y_sup_izq > 0:
            self.__y_sup_izq -= s 
        self.__y_inf_der -= s