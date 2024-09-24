import flet
import os.path
from elevate import elevate
from time import sleep
from os import remove
from flet import *

elevate( show_console = False )
def main( page: Page ):

    page.window.resizable = False
    page.window.width = 400
    page.window.height = 400

    def OpenF( e = None ):
        os.system( 'explorer.exe GoodByeDPI' )

    def Stop( e = None ):
        os.system( 'taskkill /IM goodbyedpi.exe /F' )
        contentContainer.content.controls.remove( StopBTN )
        contentContainer.content.controls.append( StartBTN )
        contentContainer.content.controls.append( empty )
        contentContainer.content.controls.append( pInput )
        contentContainer.content.controls.append( StartWP_BTN )
        contentContainer.content.controls.append( OpenBTN )
        page.update()

    def Start( e = None ):
        file_path = "GoodByeDPI/1_russia_blacklist.bat"
        fileEx = os.path.exists( file_path )
        if fileEx == True:
            os.system( 'cd GoodByeDPI & 1_russia_blacklist.bat' )
            contentContainer.content.controls.remove( StartBTN )
            contentContainer.content.controls.remove( StartWP_BTN )
            contentContainer.content.controls.remove( pInput )
            contentContainer.content.controls.remove( empty )
            contentContainer.content.controls.remove( OpenBTN )
            contentContainer.content.controls.append( StopBTN )
            page.update()
        else:
            cmdFile = open( 'GoodByeDPI/1_russia_blacklist.txt', 'w+' )
            cmdFile.write( '@ECHO OFF\n'
                           'PUSHD "%~dp0"\n'
                           'set _arch=x86\n'
                           'IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (set _arch=x86_64)\n'
                           'IF DEFINED PROCESSOR_ARCHITEW6432 (set _arch=x86_64)\n'
                           'PUSHD "%_arch%"\n'
                           '\n'
                           'start "" goodbyedpi.exe -1 --blacklist ../russia-blacklist.txt --blacklist ../russia-youtube.txt\n'
                           '\n'
                           'POPD\n'
                           'POPD' )
            cmdFile.close()
            os.rename( 'GoodByeDPI/1_russia_blacklist.txt', 'GoodByeDPI/1_russia_blacklist.bat' )
            os.system( 'cd GoodByeDPI & 1_russia_blacklist.bat' )
            contentContainer.content.controls.remove( StartBTN )
            contentContainer.content.controls.remove( StartWP_BTN )
            contentContainer.content.controls.remove( pInput )
            contentContainer.content.controls.remove( empty )
            contentContainer.content.controls.remove( OpenBTN )
            contentContainer.content.controls.append( StopBTN )
            page.update()

    def StartWithP( e = None ):
        getP = str( pInput.value )
        file_path = "GoodByeDPI/1_russia_blacklist.bat"
        fileEx = os.path.exists( file_path )
        if fileEx == False:
            cmdFile = open( 'GoodByeDPI/1_russia_blacklist.txt', 'w+' )
            cmdFile.write( '@ECHO OFF\n'
                           'PUSHD "%~dp0"\n'
                           'set _arch=x86\n'
                           'IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (set _arch=x86_64)\n'
                           'IF DEFINED PROCESSOR_ARCHITEW6432 (set _arch=x86_64)\n'
                           'PUSHD "%_arch%"\n'
                           '\n'
                           f'start "" goodbyedpi.exe { getP } --blacklist ../russia-blacklist.txt --blacklist ../russia-youtube.txt\n'
                           '\n'
                           'POPD\n'
                           'POPD' )
            cmdFile.close()
            sleep( 1 )
            os.rename( 'GoodByeDPI/1_russia_blacklist.txt', 'GoodByeDPI/1_russia_blacklist.bat' )
            os.system( 'cd GoodByeDPI & 1_russia_blacklist.bat' )
            contentContainer.content.controls.remove( StartBTN )
            contentContainer.content.controls.remove( StartWP_BTN )
            contentContainer.content.controls.remove( pInput )
            contentContainer.content.controls.remove( empty )
            contentContainer.content.controls.remove( OpenBTN )
            contentContainer.content.controls.append( StopBTN )
            page.update()
        else:
            os.remove( 'GoodByeDPI/1_russia_blacklist.bat' )
            cmdFile = open( 'GoodByeDPI/1_russia_blacklist.txt', 'w+' )
            cmdFile.write( '@ECHO OFF\n'
                           'PUSHD "%~dp0"\n'
                           'set _arch=x86\n'
                           'IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (set _arch=x86_64)\n'
                           'IF DEFINED PROCESSOR_ARCHITEW6432 (set _arch=x86_64)\n'
                           'PUSHD "%_arch%"\n'
                           '\n'
                           f'start "" goodbyedpi.exe { getP } --blacklist ../russia-blacklist.txt --blacklist ../russia-youtube.txt\n'
                           '\n'
                           'POPD\n'
                           'POPD' )
            cmdFile.close()
            sleep( 1 )
            os.rename( 'GoodByeDPI/1_russia_blacklist.txt', 'GoodByeDPI/1_russia_blacklist.bat' )
            os.system( 'cd GoodByeDPI & 1_russia_blacklist.bat' )
            contentContainer.content.controls.remove( StartBTN )
            contentContainer.content.controls.remove( StartWP_BTN )
            contentContainer.content.controls.remove( pInput )
            contentContainer.content.controls.remove( empty )
            contentContainer.content.controls.remove( OpenBTN )
            contentContainer.content.controls.append( StopBTN )
            page.update()


    pInput = TextField(
        hint_text = 'Enter launch parameter...',
        width = 300,
        height = 40,
        border_radius = 10,
        border_color = '#33A3AD',
    )

    empty = Container( height = 40 )

    StartWP_BTN = FilledButton(
                    text = 'Start With Parameter',
                    width = 300,
                    height = 40,
                    style = ButtonStyle(
                        bgcolor = '#33A3AD',
                        shape = RoundedRectangleBorder( radius = 10 )
                    ),
                    on_click = lambda e: StartWithP()
                )
    StartBTN = FilledButton(
                    text = 'Start',
                    width = 300,
                    height = 40,
                    style = ButtonStyle(
                        bgcolor = '#33A3AD',
                        shape = RoundedRectangleBorder( radius = 10 )
                    ),
                    on_click = lambda e: Start()
                )

    StopBTN = FilledButton(
                    text = 'Stop | Update',
                    width = 300,
                    height = 40,
                    style = ButtonStyle(
                        bgcolor = '#33A3AD',
                        shape = RoundedRectangleBorder( radius = 10 )
                    ),
                    on_click = lambda e: Stop()
                )

    OpenBTN = FilledButton(
                    text = 'Open GB DPI Folder',
                    width = 300,
                    height = 35,
                    style = ButtonStyle(
                        bgcolor = '#3e8790',
                        shape = RoundedRectangleBorder( radius = 10 )
                    ),
                    on_click = lambda e: OpenF()
                )

    # container for content
    contentContainer = Container(
        width = 375,
        height = 350,
        padding = padding.only( left = 75, right = 75 ),
        bgcolor = '#444A4B',
        border_radius = 10,
        content = Column( alignment = 'center',
                       controls = [
                           StartBTN,
                           empty,
                           pInput,
                           StartWP_BTN,
                           OpenBTN
                        ]
                )
    )

    # main container ( main window )
    mainContainer = Container(
        expand = True,
        margin = -10,
        padding = 5,
        bgcolor = '#33A3AD',
        content = Row(
            controls = [
                contentContainer
            ]
        )
    )

    ###
    page.add( mainContainer )
    page.update()

    pass


if __name__ == '__main__':
    flet.app( target = main )