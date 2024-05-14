import os
import subprocess
from pathlib import Path
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem, SubmenuItem, CommandItem
papka_work_now = os.path.dirname(Path(__file__))

class InfoAboutScripts:
    def get_info():
        print("Объяснение работы скриптов\nНачать исправление, связанное с организацией:\nДанный скрипт, экспортирует задеваемые им ветки реестра для последующего их удаления.\n\n")
        print("Начать исправление долгой перезагрузки и долгого выключения:\nДанный скрипт, экспортирует задеваемые им ветки реестра для последующего изменения значений ключей реестра.\n\n ")
        print("Перезапуск произойдет сразу после выполнения скрипта, так что советую сохранить работу и закрыть программы.\n")
        input("Нажмите Enter для возврата в меню...")
        

class RepairWindows:
    def repair_organization_problem():
        export_papka_for_repair = "Repair Windows"
        if not os.path.exists(export_papka_for_repair):
            os.makedirs(export_papka_for_repair)
        vetki_for_repair_windows = [
            "HKCU\\Software\\Microsoft\\WindowsSelfHost",
            "HKCU\\Software\\Policies",
            "HKLM\\Software\\Microsoft\\Policies",
            "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies",
            "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsStore\\WindowsUpdate",
            "HKLM\\Software\\Microsoft\\WindowsSelfHost",
            "HKLM\\Software\\Policies",
            "HKLM\\Software\\WOW6432Node\\Microsoft\\Policies",
            "HKLM\\Software\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies",
            "HKLM\\Software\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\WindowsStore\\WindowsUpdate"
            ]
        for vetka_policies in vetki_for_repair_windows:
            name_of_file = vetka_policies.replace("\\", "_") + ".reg"
            command_export_repair_windows = f'REG EXPORT "{vetka_policies}" "{papka_work_now}\\{export_papka_for_repair}\\{name_of_file}" /y'
            command_delete = f'REG DELETE "{vetka_policies}" /f'
            subprocess.Popen('cmd /k {command_export_repair_windows}'.format(command_export_repair_windows=command_export_repair_windows), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.Popen('cmd /k {command_delete}'.format(command_delete=command_delete), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.Popen('cmd /k shutdown /r /t 0'.format(command=command), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        
    def repair_boot_problem():
        export_papka_for_reboot = "Repair Reboot Windows"
        if not os.path.exists(export_papka_for_reboot):
            os.makedirs(export_papka_for_reboot)
        vetki_for_repair_boot_windows = [
            "HKLM\\SYSTEM\\CurrentControlSet\\Control",
            "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
            "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters",
            "HKLM\\SYSTEM\\ControlSet001\\Services\\Ndu",
            "HKLM\\SYSTEM\\ControlSet001\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\be337238-0d82-4146-a960-4f3749d470c7"
        ]
        commands_for_rewrite = [
            "WaitToKillServiceTimeout", 
            "ClearPageFileAtShutdown",  
            "EnablePrefetcher",         
            "Start",                    
            "Attributes"                
        ]
        values = [
            5000,
            0,
            5,
            4,
            2
        ]
        types = [
            "REG_SZ",
            "REG_DWORD",
            "REG_DWORD",
            "REG_DWORD",
            "REG_DWORD"
        ]
        for vetka_for_repair_boot_windows in vetki_for_repair_boot_windows:
            name_of_file = vetka_for_repair_boot_windows.replace("\\", "_") + ".reg"
            command_for_export_boot_vetki = f'REG EXPORT "{vetka_for_repair_boot_windows}" "{papka_work_now}\\{export_papka_for_reboot}\\{name_of_file}" /y'
            subprocess.Popen('cmd /k {command_for_export_boot_vetki}'.format(command_for_export_boot_vetki=command_for_export_boot_vetki), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        for i in range(len(vetki_for_repair_boot_windows)):
            command = commands_for_rewrite[i]
            value = values[i]
            type_ = types[i]
            command_rewrite_regedit = f'REG ADD "{vetki_for_repair_boot_windows[i]}" /v "{command}" /t {type_} /d {value} /f'
            subprocess.Popen('cmd /k {command_rewrite_regedit}'.format(command_rewrite_regedit=command_rewrite_regedit), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.Popen('cmd /k shutdown /r /t 0'.format(command=command), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

class InfoAboutMe:
    def get_info():
        print("Код написан: MaximDev a.k.a. MaxonKlaxon\n")
        print("Github:https://github.com/MAX1MDEV")
        print("Discord:https://discordapp.com/users/390102465586003978/\n")
        input("Нажмите Enter для возврата в меню...")

if __name__ == '__main__':
    menu = CursesMenu("Вас приветствует скрипт Repair Windows", "Выберите пункт меню: ")
    function1_item = FunctionItem("Узнать информацию о нижеперечисленных скриптах", InfoAboutScripts.get_info)
    function2_item = FunctionItem("Начать исправление, связанное с организацией", RepairWindows.repair_organization_problem)
    function3_item = FunctionItem("Начать исправление долгой перезагрузки и долгого выключения", RepairWindows.repair_boot_problem)
    function4_item = FunctionItem("Инфо", InfoAboutMe.get_info)
    menu.items.append(function1_item)
    menu.items.append(function2_item)
    menu.items.append(function3_item)
    menu.items.append(function4_item)
    menu.show()