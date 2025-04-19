# Simulador de Créditos Educativos

## Autores:
- Juan Sebastián Pinilla
- Mileidy Vanegas
- Samuel Gil

## Autores de la interfaz gráfica:
- Emanuel García
- Luis Carlos Guerra

## Descripción

Este programa permite a los estudiantes conocer con claridad su compromiso financiero y planificar sus pagos de manera adecuada. La simulación calcula la cantidad que el estudiante debe pagar mientras estudia y el monto que debe cancelar después de finalizar su periodo de estudios. La información para la realización de este programa fue extraida directamente de la página del [ICETEX](https://web.icetex.gov.co/es/creditos/tu-eliges).

## Entradas

El programa recibe los siguientes datos de entrada:

- **Tipo de crédito**: Puede ser:
  - "Mediano Plazo - 30%"
  - "Mediano Plazo - 60%"
  - "Corto Plazo - 100%"
- **Valor total de la carrera**: Costo total de los estudios en pesos colombianos.
- **Duración en años**: Tiempo estimado de duración del programa de estudios.

## Proceso

El programa sigue estos pasos:

1. Se selecciona el tipo de crédito.
2. Se aplican las reglas según el tipo de crédito elegido:

   - **Mediano Plazo - 30%**:
     - El estudiante paga el 30% del costo total mientras estudia.
     - Al finalizar, debe pagar el 70% restante en un tiempo equivalente a **1.5 veces** la duración de la carrera.
     - IPC + 9% que equivale al 1,15% mes vencido (14,67% efectivo anual). La tasa efectiva anual del 14,67% es equivalente al 13,77% Nominal Anual Mes Vencido. 

   - **Mediano Plazo - 60%**:
     - El estudiante paga el 60% mientras estudia.
     - Al finalizar, debe pagar el 40% restante en un tiempo equivalente a **1.5 veces** la duración de la carrera.
     - IPC + 7%, que equivale al 0,99%mes vencido (12,56% efectivo anual). La tasa efectiva anual del 12,56% es equivalente al 11,89% Nominal Anual Mes Vencido. 

   - **Corto Plazo - 100%**:
     - El estudiante paga el **100%** del costo total durante el periodo de estudio.
     - IPC + 7%, que equivale al 0,99%mes vencido (12,56% efectivo anual). La tasa efectiva anual del 12,56% es equivalente al 11,89% Nominal Anual Mes Vencido. 

3. Se calculan los montos a pagar en cada etapa según la selección del usuario.

## Salidas

El programa genera los siguientes resultados:

- **Pago durante el periodo de estudios**: Cantidad total a pagar mientras el estudiante cursa la carrera.
- **Pago posterior al periodo de estudios**: Monto total restante a pagar después de finalizar los estudios.

## Ejemplo de Uso

Si un estudiante selecciona el crédito **"Mediano Plazo - 30%"** para una carrera de **5 años** con un costo de **50,000,000 COP**:

- **Pago durante los estudios**:  
  *30% de 50,000,000 = 15,000,000 COP + intereses*
- **Pago después de los estudios**:  
  *70% de 50,000,000 = 35,000,000 COP + intereres*
- **Tiempo para pagar el saldo restante**:  
  *5 años * 1.5 = 7.5 años*

Este programa permite a los estudiantes conocer con claridad su compromiso financiero y planificar sus pagos de manera adecuada.

## Fórmulas Utilizadas

El cálculo de los pagos se basa en la fórmula de cuotas fijas de un crédito con tasa de interés mensual:

$$P = \frac{C \cdot r}{1 - (1 + r)^{-n}}$$

Donde:
- **P** es el pago mensual.
- **C** es el capital total financiado (dependiendo del tipo de crédito, puede ser el 30%, 60% o 100% del costo de la carrera).
- **r** es la tasa de interés mensual:
  - 1,15% (0,0115) para **Mediano Plazo - 30%**.
  - 0,99% (0,0099) para **Mediano Plazo - 60%** y **Corto Plazo - 100%**.
- **n** es el número de meses de pago (durante el estudio o después, según corresponda).

### **Cálculo del Pago Durante el Estudio**
Para los créditos de **Mediano Plazo - 30%** y **Mediano Plazo - 60%**, el estudiante paga una parte del crédito mientras estudia, calculado con la fórmula:

$$
P = \frac{(p_c \cdot C) \cdot r}{1 - (1 + r)^{-m}}
$$

Donde:
- **p_c** es el porcentaje del costo total cubierto mientras estudia (30% o 60% según el crédito).
- **m** es el número de meses durante el estudio (**semestres × 6 meses**).

### **Cálculo del Pago Después del Estudio**
Para los créditos de **Mediano Plazo - 30%** y **Mediano Plazo - 60%**, al finalizar los estudios, el saldo restante se paga en un tiempo equivalente a **1.5 veces la duración de la carrera**:

$$
P = \frac{(p_f \cdot C) \cdot r}{1 - (1 + r)^{-m_f}}
$$

Donde:
- **p_f** es el porcentaje restante del crédito (70% o 40% según el crédito).
- **m_f** es el número de meses para pagar después del estudio (**1.5 × duración en años × 12 meses**).

### **Corto Plazo - 100%**
En este tipo de crédito, el estudiante paga el **100% del costo total** durante el periodo de estudio. Se calcula con la misma fórmula:

$$
P = \frac{C \cdot r}{1 - (1 + r)^{-m}}
$$

Donde **m** es el número de meses durante la carrera (**semestres × 6 meses**).

---
Este programa utiliza estas fórmulas para calcular el compromiso financiero de los estudiantes y ayudarlos a planificar sus pagos de manera adecuada.


## Ejecución del Proyecto

Para ejecutar la interfaz en consola, use el siguiente comando:

```sh
python src/view/console/main.py
```
## Ejecución de Interfaz Gráfica Kivy

Para ejecutar las interfaz gráfica, utilice el siguiente comando desde la raíz del proyecto:

```sh
python src/view/gui/console_kivy.py
```

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias, utilice el siguiente comando desde la raíz del proyecto:

```sh
python -m unittest discover -s tests -p "test_*.py"
```

## Ejecutable del proyecto

### Pasos para ejecutar SimuladorIcetex.exe

1. **Ubicación del archivo**
   - Navegar a la carpeta dist dentro del proyecto:
   ```batch
   cd icetex_simulator_kivy\dist
   ```

2. **Verificar requisitos previos**
   - Asegurarse de tener Python 3.12 instalado
   - Todas las dependencias listadas en requirements.txt deben estar instaladas
   - Windows debe tener las bibliotecas visuales de C++ instaladas

3. **Ejecutar el programa**
   - Doble clic en `SimuladorIcetex.exe`
   - O desde la línea de comandos:
   ```batch
   SimuladorIcetex.exe
   ```


## Estructura del Proyecto

```python
icetex_simulator_kivy/
│
├── assets/
│   ├── icetex.ico
│
├── build/  # Carpeta generada por PyInstaller 
│
├── dist/
│   ├── SimuladorIcetex.exe   
│
├── src/
│   ├── controller/
│   │   ├── __init__.py
│   │   
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   ├── Casos de Prueba.xlsx
│   │   ├── exception.py
│   │   └── logic.py
│   │
│   └── view/
│       ├── console/
│       │   └── main.py
│       ├── gui/
│       │   └── console_kivy.py
│       └── web/
│           └── app.py
│
├── test/
│   └── test_logic.py
│
├── .gitignore
├── config.py
├── launch.py
├── README.md
├── requirements.txt
└── SimuladorIcetex.spec

```
