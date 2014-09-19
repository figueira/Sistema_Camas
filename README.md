Sistema de Gestión de Camas
===========================
Módulo de Gestión de Camas del sistema desarrollado como MiniProyecto de Desarollo de Software en la Universidad Simón Bolívar para el Centro Médico de Caracas.

----
---:Última modificación: 20 de junio de 2014. Karen Troiano, Rebeca Machado, Ronier Rodríguez y Leonardo Ramos.

Directorios
===========
	- AM: Carpeta principal con el settings.py y la configuración del proyecto.
	- app_camas:  Archivos relacionados con el manejo de las habitaciones.
		En el models se encuentran las entidades Ingreso y Habitacion.
	- app_estadisticas: Archivos relacionados con el manejo de las estadisticas del sistema.
		Actualmente sólo se maneja el termómetro y la matriz de habitaciones.
	- app_paciente: Archivos relacionados con el manejo de los pacientes del sistema.
		En el models se encuentran la entidad Paciente.
	- app_solicitudes: Archivos relacionados con el manejo de las solicitudes de camas.
		En el models se encuentran la entidad Solicitud.
	- app_usuario: Archivos relacionados con usuarios del sistema.
		En el models se encuentran las entidades Médico y Usuario.
	
	- recursos: 
        - base de datos: Contiene los generadores de datos para poblar la base de datos y las listas
        otorgadas por el cliente para generar las enfermedades y el directorio médico del hospital.		
		- configuracion: Contiene el archivo settings que deberá ser debidamente modificado y colocado
        en la carpeta AM. Además, un archivo con varios comandos útiles para el programador.
        - documentacion: Se encuentran todos los documentos y diagramas del sistema en su versión
        final y editable. Esta carpeta es sumamente importante para el desarrollo y mantenimiento
        del sistema.
		- manuales: Manual de instalación en Windows en su versión final y editable.

	- static:
		- css: Hojas de estilo del sistema.
		- img: Imágenes utilizadas en el sistema.
        - js: Scripts realizados para el sistema.
		- libs: Librerías utilizadas. Cada una posee su propia estructura css-img-js interna.
		
	- templates: Archivos htmls del sistema.


Bibliografía/enlaces recomendados
=================================
	https://www.djangoproject.com/
	http://www.djangobook.com/en/2.0/index.html
	http://aiti.mit.edu/media/programs/mexico-summer-2013/materials/djangobook.pdf