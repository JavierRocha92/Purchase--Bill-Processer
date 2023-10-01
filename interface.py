# importamos las libreia quw noa hacen falta
import kivy
# indicamos la version minima requerida
kivy.require('1.9.0')
# importamos libreria especificas
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# para tamaño de la ventna 
from kivy.config import Config
# para la condiguracion del ancho de la ventana
Config.set('graphics','width',400)
# para la condiguracion del alto de la ventana
Config.set('graphics','height',200)
# creamos la primera capa que se llamara container y que hereda de BoxLayout
class Container(BoxLayout):
    None
    # con este valor le estamos dejando vacio y no realizata ninguna accion
    
# creamos la ventana principal que le damos el nombre de main el mismo que el archivo .kv
class Main(App):
    title = 'main'
    # esta funcionn en la primera que va a ejecutar cuando este dentro de ests ventana
    # y nos va a devolver el contenedor principal
    def build(self):
        return Container()
    
if __name__ == '__main__':
    # utilizamos este metodo para correr la ventana con la que lo edtamos llamando
    # en este cado con la ventana main
    Main().run()
    
    