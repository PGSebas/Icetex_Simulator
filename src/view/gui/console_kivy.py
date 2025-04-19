import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from model.logic import (
    payment_fee_calc_while_studying, payment_fee_calc_after_studying
)
from model.exception import *

class Icetex_Calculator(App):
    def build(self):
        """
        Construye la interfaz gráfica de la aplicación ICETEX Simulator.

        Crea y organiza los elementos de la interfaz, como botones, etiquetas, 
        entradas de texto y contenedores. También configura el fondo y el diseño general.

        Returns:
            BoxLayout: El contenedor principal de la interfaz.
        """
        main_container = BoxLayout(orientation="vertical")
        
        # Agregar un color de fondo usando Canvas
        with main_container.canvas.before:
            Color((230 / 255), (230 / 255), (230 / 255), 1)  # Convertir RGB a valores entre 0 y 1
            self.rect = Rectangle(pos=main_container.pos, size=main_container.size)
            
        def update_rect(instance, value):
            """
            Actualiza la posición y el tamaño del fondo cuando el contenedor principal cambia.

            Args:
                instance: La instancia del contenedor principal.
                value: El valor actualizado (posición o tamaño).
            """
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        
        main_container.bind(pos=update_rect, size=update_rect)

        title_welcome = Label(text="Welcome to the ICETEX simulator", color=(0, 0, 0, 1), font_size=30)

        container_tittle_welcome = AnchorLayout(anchor_x="center", anchor_y="center")
        container_tittle_welcome.add_widget(title_welcome)
        
        credit_title = Label(text="Choose your credit type", color=(0, 0, 0, 1), font_size=19)

        # Contenedor de botones con espaciado
        self.container_buttons = BoxLayout(orientation="horizontal", spacing=20, size_hint=(None, None)) 

        # Botones para el tipo de crédito
        btn_30_porcentage = Button(
            text="30 %",
            background_color=(0, 0.7, 1, 1),
            size_hint=(None, None),  
            size=(200, 50)         
        )
        btn_30_porcentage.bind(on_press= self.select_credit_type)
        
        btn_60_porcentage = Button(
            text="60 %",
            background_color=(0, 0.7, 1, 1),
            size_hint=(None, None),
            size=(200, 50)
        )
        btn_60_porcentage.bind(on_press = self.select_credit_type)
        
        btn_100_porcentage = Button(
            text="100 %",
            background_color=(0, 0.7, 1, 1),
            size_hint=(None, None),
            size=(200, 50)
        )
        btn_100_porcentage.bind(on_press = self.select_credit_type)

        # Añadir botones al contenedor de botones
        self.container_buttons.add_widget(btn_30_porcentage)
        self.container_buttons.add_widget(btn_60_porcentage)
        self.container_buttons.add_widget(btn_100_porcentage)

        # Calcular el tamaño total del contenedor de botones
        self.container_buttons.size = (660, 50)  # Ancho total = suma de los anchos de los botones + espaciado

        # Centrar el contenedor de botones usando AnchorLayout
        centered_container = AnchorLayout(anchor_x="center", anchor_y="center")
        centered_container.add_widget(self.container_buttons)

        # Entradas para el semestre
        layout_input_cost = AnchorLayout(anchor_x="center", anchor_y="center")
        layout_input_quantity = AnchorLayout(anchor_x="center", anchor_y="center")

        cost_semesteer_title = Label(text="Enter the cost of semester", color=(0, 0, 0, 1), font_size=19)
        quantity_semesteers_title = Label(text="Enter the number of semesters", color=(0, 0, 0, 1), font_size=19)

        self.cost_semesteer = TextInput(
            hint_text="e.g. (12000000)",
            halign="center",
            size_hint=(0.5, 0.5),
            multiline=False,
            input_filter='float'
        )
        self.quantity_semesteer = TextInput(
            hint_text="e.g. (10)",
            halign="center",
            size_hint=(0.5, 0.5),
            multiline=False,
            input_filter='int'
        )

        layout_input_cost.add_widget(self.cost_semesteer)
        layout_input_quantity.add_widget(self.quantity_semesteer)
        
        container_button_controller = GridLayout(cols=2, spacing=20, size_hint=(None, None))
        calculate = Button(
            text="Calculate",
            background_color=(0, 0.78, 0.25, 0.9),
            size_hint=(None, None), size=(200, 50)
        )
        calculate.bind(on_press=self.calculate)
        
        
        restart = Button(text='Restart', background_color=(0.86, 0.13, 0, 0.9), size_hint=(None, None), size=(200, 50))
        restart.bind(on_press=self.restart)
        
        container_button_controller.add_widget(restart)
        container_button_controller.add_widget(calculate)
        
        container_button_controller.size = (440, 50)
        
        centered_container_controller = AnchorLayout(anchor_x="center", anchor_y="center")
        centered_container_controller.add_widget(container_button_controller)
        
        container_output = BoxLayout()
        self.output = Label(text="Total credit: ", halign="center", color=(0, 0, 0, 1), font_size=19)
        container_output.add_widget(self.output)
        

        # Añadir widgets al contenedor principal
        main_container.add_widget(container_tittle_welcome)
        main_container.add_widget(credit_title)
        main_container.add_widget(centered_container)  # Añadir el contenedor centrado
        main_container.add_widget(cost_semesteer_title)
        main_container.add_widget(layout_input_cost)
        main_container.add_widget(quantity_semesteers_title)
        main_container.add_widget(layout_input_quantity)
        main_container.add_widget(container_output)
        main_container.add_widget(centered_container_controller)
        self.credit_type_choice = 0
        
        return main_container

    def select_credit_type(self, sender):
        """
        Maneja la selección del tipo de crédito.

        Deshabilita todos los botones cuando el usuario selecciona una opción y cambia el color de fondo del boton pulsado.
        También almacena el tipo de crédito seleccionado.

        Args:
            sender (Button): El botón que fue presionado.
        """
        self.credit_type_choice = 0
        for button in self.container_buttons.children:
            button.disabled = True

        # Determinar el tipo de crédito basado en el texto del botón
        if sender.text == "30 %":
            self.credit_type_choice = 1
            sender.background_color = (0.15, 0.96, 0, 1)
        elif sender.text == "60 %":
            self.credit_type_choice = 2
            sender.background_color = (0.15, 0.96, 0, 1)
        elif sender.text == "100 %":
            self.credit_type_choice = 3
            sender.background_color = (0.15, 0.96, 0, 1)

        # Imprimir el tipo de crédito seleccionado
        print(self.credit_type_choice)
                
    def calculate(self, sender):
        """
        Calcula el total del crédito basado en los datos ingresados.

        Usa el tipo de crédito seleccionado, el costo del semestre y el número de semestres
        para calcular el total del crédito mientras esta estudiando y despues de terminar.

        Args:
            sender (Button): El botón que fue presionado.
        """
        try:  
            if not self.credit_type_choice:
                raise NotPressBottonError
            credit_type = self.credit_type_choice
            
            if not self.cost_semesteer.text:
                raise CollegeEnrollmentError
            college_enrollment = float(self.cost_semesteer.text)
            if college_enrollment < 0:  # We make ensure it is a positive number
                raise CollegeEnrollmentMenorThanZeroError()
            
            
            if not self.quantity_semesteer.text:
                raise SemestersError()
            semesters = int(self.quantity_semesteer.text)
            if semesters > 12:
                raise SemestersError()
            if semesters < 0:
                raise SemestersError()
            
            fee_while_studying = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)
            fee_after_studying = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)
            
            if not fee_after_studying:
                self.output.text = f"Total credit: \nYour monthly fee while studying is: ${round(fee_while_studying, 2)}\n"
            else:
                self.output.text = f"Total credit: \nYour monthly fee while studying is: ${round(fee_while_studying, 2)}\nYour monthly fee after studying is: ${round(fee_after_studying, 2)}\n"
            
        except (CollegeEnrollmentError, ValueError, SemestersError, CreditTypeError, CollegeEnrollmentMenorThanZeroError, NotPressBottonError) as e:
            self.show_error(str(e))

        
    
    def restart(self, sender):
        """
        Reinicia la aplicación a su estado inicial.

        Habilita todos los botones y restablece los colores y el texto de salida.

        Args:
            sender (Button): El botón que fue presionado.
        """
        for button in self.container_buttons.children:
            button.disabled = False
            button.background_color = (0, 0.7, 1, 1)
            self.credit_type_choice = 0
        
        self.cost_semesteer.text = ""
        self.quantity_semesteer.text = ""
        self.output.text = "Total credit: "
    
    def show_error( self, err ):
        """ 
        Abre una ventana emergente, con un texto y un botón para cerrar 
        Parámetros: 
        err: Mensaje de error que queremos mostrar en la ventana        
        """
        
        content = BoxLayout(orientation='vertical', padding=50, spacing=10)
        content.bind(minimum_height=content.setter('height'))
    
        # Etiqueta con texto adaptado al tamaño de la pantalla
        error_label = Label(text=str(err), size_hint=(1,None), halign="center", valign="middle", text_size=(400,None))
        error_label.bind(texture_size=error_label.setter('size'))
        content.add_widget( error_label )

        container_button_close = AnchorLayout(anchor_x="center", anchor_y="bottom")
        close = Button(text="Close", size_hint=(None,None), size=(200,50))
        container_button_close.add_widget(close)
        content.add_widget(container_button_close)
        
        # Crear el Popup con tamaño reducido
        popup = Popup(title="Error",content=content, size_hint=(None,None), size=(450,300), auto_dismiss=False)
        
        close.bind( on_press=popup.dismiss)
        
        popup.open()
   
    
if __name__ == "__main__":
    Icetex_Calculator().run()