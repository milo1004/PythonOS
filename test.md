flowchart TB
    %% Initialization Layer
    subgraph "Initialization Layer"
        style Initialization Layer fill:#D6EAF8,stroke:#1B4F72
        Activate["activate.sh"]:::boot
        SHS_Boot1["shs/boot.sh"]:::boot
        SHS_Boot2["shs/boot2.sh"]:::boot
        SHS_Boot3["shs/boot3.sh"]:::boot
        SHS_Boot4["shs/boot4.sh"]:::boot
        BootPy["boot.py"]:::boot
        SetupPy["setup.py"]:::boot
        InstallBoot["install.py"]:::boot
        LogonBoot["logon.py"]:::boot
        ShowInfo["show_info.py"]:::boot
    end

    %% Core Layer
    subgraph "Core Layer"
        style Core Layer fill:#D5F5E3,stroke:#145A32
        Main["main.py"]:::core
        Central["central.py"]:::core
    end

    %% Execution Layer
    subgraph "Execution Layer"
        style Execution Layer fill:#FCF3CF,stroke:#7D6608
        subgraph "Commands"
            style Commands fill:#FDEBD0,stroke:#B9770E
            Cat["cat"]:::command
            Dir["dir"]:::command
            SysInstall["sysinstall"]:::command
        end
        FS_Cat["cat.py"]:::command
        FS_Dir["dir.py"]:::command
        SysInstFile["sysinstall.py"]:::command
    end

    %% Data Stores
    subgraph "Data Stores"
        style Data Stores fill:#EBDEF0,stroke:#4A235A
        Passwd["passwd.txt"]:::store
        Username["username.txt"]:::store
        Packages["packages.txt"]:::store
    end

    %% External Libraries
    ExtLibs["External Libraries\n(climage, hex, pyfiglet)"]:::external

    %% Connections
    Activate -->|calls| BootPy
    SHS_Boot1 --> BootPy
    SHS_Boot2 --> BootPy
    SHS_Boot3 --> BootPy
    SHS_Boot4 --> BootPy
    BootPy --> SetupPy
    SetupPy --> InstallBoot
    InstallBoot --> LogonBoot
    LogonBoot --> ShowInfo
    ShowInfo --> Central

    Main --> Central
    Central -->|dispatch| Cat
    Central -->|dispatch| Dir
    Central -->|invoke| SysInstall

    Cat --> FS_Cat
    Dir --> FS_Dir
    SysInstall --> SysInstFile

    Central -->|reads/writes| Passwd
    Central -->|reads/writes| Username
    SysInstall --> Packages
    Central --> ExtLibs
    Cat --> ExtLibs
    Dir --> ExtLibs

    %% Click Events - Boot Loader Layer
    click Activate "https://github.com/milo1004/pythonos/blob/main/./activate.sh"
    click SHS_Boot1 "https://github.com/milo1004/pythonos/blob/main/./PythOS/shs/boot.sh"
    click SHS_Boot2 "https://github.com/milo1004/pythonos/blob/main/./PythOS/shs/boot2.sh"
    click SHS_Boot3 "https://github.com/milo1004/pythonos/blob/main/./PythOS/shs/boot3.sh"
    click SHS_Boot4 "https://github.com/milo1004/pythonos/blob/main/./PythOS/shs/boot4.sh"
    click BootPy "https://github.com/milo1004/pythonos/blob/main/./PythOS/boot/boot.py"
    click SetupPy "https://github.com/milo1004/pythonos/blob/main/./PythOS/boot/setup.py"
    click InstallBoot "https://github.com/milo1004/pythonos/blob/main/./PythOS/boot/install.py"
    click LogonBoot "https://github.com/milo1004/pythonos/blob/main/./PythOS/boot/logon.py"
    click ShowInfo "https://github.com/milo1004/pythonos/blob/main/./PythOS/boot/show_info.py"

    %% Click Events - Core Layer
    click Central "https://github.com/milo1004/pythonos/blob/main/./PythOS/central.py"
    click Main "https://github.com/milo1004/pythonos/blob/main/./main.py"

    %% Click Events - Command Modules
    click FS_Cat "https://github.com/milo1004/pythonos/blob/main/./PythOS/bin/cat/cat.py"
    click FS_Dir "https://github.com/milo1004/pythonos/blob/main/./PythOS/bin/dir/dir.py"
    click SysInstFile "https://github.com/milo1004/pythonos/blob/main/./PythOS/bin/sysinstall/sysinstall.py"

    %% Click Events - Data Stores
    click Passwd "https://github.com/milo1004/pythonos/blob/main/./PythOS/userdata/passwd.txt"
    click Username "https://github.com/milo1004/pythonos/blob/main/./PythOS/userdata/username.txt"
    click Packages "https://github.com/milo1004/pythonos/blob/main/./PythOS/packages.txt"

    %% Styles
    classDef boot fill:#AED6F1,stroke:#1B4F72,color:#1B2631,stroke-width:2px
    classDef core fill:#A9DFBF,stroke:#145A32,color:#0E6251,stroke-width:2px
    classDef command fill:#F9E79F,stroke:#B9770E,color:#7D6608,stroke-width:2px
    classDef store fill:#D2B4DE,stroke:#4A235A,color:#4A235A,stroke-width:2px
    classDef external fill:#E8DAEF,stroke:#4A235A,color:#512E5F,stroke-width:2px