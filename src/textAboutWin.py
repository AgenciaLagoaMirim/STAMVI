class TextAboutWin:
    def __init__(self):

        self.TEXT_0 = """
        Agência para o Desenvolvimento da Bacia da Lagoa Mirim - ALM
        Universidade Federal de Pelotas - UFPel
        Núcleo de Ensino Pesquisa e Extensão - NEPE HIDROSEDI
        """

        self.TEXT_1 = """
        STAMVI - Sistema de Tratamento de dados para a Aplicação do Método das Velocidades Indexadas.
        Follow the steps below to use STAMVI:\n
        1 - In the "Export Processed Data as" field, choose the file extension type to which you want to export the data.\n
        2 - In the "Load WorkSpace" field, select the file exported in step 1. The data will be available for visualization in "Final DataFrame Display."\n
        3 - In the "Execute Models" field, the "Area" button runs the "Stage-Area Rating" model, and the "Avg. Velocity" button runs the "Index Velocity - Average Velocity Rating" model.\n
        The "NSE" button displays the Nash-Sutcliffe coefficient.\n
        4 - In the "Time Series" field, by clicking the respective button and selecting the folder with .dat file extension files, historical series will be plotted.\n
        In "Discharge," in addition to graph plotting, it is possible to export the estimated data in .xlsx format.\n
        -----------------------------------------------------------------------------------------------------------------
        Source code and development:\n
        Jamilson do Nascimento
        github.com/kkcortez-nscmnt
        jamil.pyhidrodev@gmail.com
        ---------------------------------------------------------------------------------
        Development:\n
        Gilberto Loguercio Collares
        gilbertocollares@gmail.com \n
        Guilherme Kruger Bartels
        guilhermebartels@gmail.com \n
        George Marino Soares Gonçalves
        george.marino.goncalves@gmail.com
        ----------------------------------------------------------------------
        icon : <a href="https://www.flaticon.com/free-icons/air-flow" title="air flow icons">Air flow icons created by Freepik - Flaticon</a>
        ----------------------------------------------------------------------
        Universidade Federal de Pelotas - UFPel https://portal.ufpel.edu.br
        NEPE - HidroSedi http://www.hidrosedi.com
        Agência para o Desenvolvimento da Bacia da Lagoa Mirim - São Gonçalo.https://agencialagoamirim.com.br
        """

        self.TEXT_2 = """
        Select a folder containing files with .xml extension,
        then select a folder containing files with .dat extension.
        That will create a .xlsx file with the processed data.
        """

        self.TEXT_3 = """
        Select a folder containing files with .xml extension,
        then select a folder containing files with .dat extension.
        That will create a .csv file with the processed data.
        """

        self.TEXT_4 = """
        Select the .xlsx or .csv file that contains the processed data.
        The data will be displayed in the Final DataFrame above.
        """

        self.TEXT_5 = """
        Runs the model for the Area(m²) - Stage (m) Rating.
        """

        self.TEXT_6 = """
        Runs the model for the Average Velocity(m/s) - Index Velocity (m/s) Rating.
        """

        self.TEXT_7 = """
        Evaluates the efficiency of the model according to the Nash-Sutcliffe coefficient.
        """

        self.TEXT_8 = """
        Obtains the time serie of  estimated Average Velocity (m/s) values from the Index Velocity - Average Velocity Rating.
        """

        self.TEXT_9 = """
        Obtains the time serie of observed Stage (m) values from .dat .
        """

        self.TEXT_10 = """
        Obtains the time serie of estimated Discharge (m³/s) values from Stage - Area Rating  and Index Velocity - Average Velocity Rating
        """
