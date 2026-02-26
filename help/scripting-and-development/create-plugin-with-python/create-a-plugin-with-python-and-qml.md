---
helpx_url: "https://helpx.adobe.com/substance-3d-sampler/scripting-and-development/create-a-plugin-with-python-and-qml.html"
breadcrumb-title: ""
description: Learn how to create plugins with Python and QML for Substance 3D Sampler to build custom user interfaces and extend functionality.
helpx_creative_field: ""
helpx_description: Sampler > Scripting and Development > Create a Plugin with Python and QML
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Create a Plugin with Python and QML
user-guide-description: ""
user-guide-title: ""
---

# Create a Plugin with Python and QML

This guide describes how to create a simple autosave plugin with Python and QML.

## Plugin structure

Sampler plugins require at least a Python and QML file in order to be imported, but other files can also be included such as images used for icons in the plugin panel. In the example below, there are 3 files:

* **autosave.py** contains the logic of the plugin and determines how it works.
* **autosave.qml** defines the appearance of the plugin in Sampler.
* **autosave.svg**is a vector graphic that is used as the icon for the plugin.

Once you have the files needed for your plugin in a single folder, you can add the plugin to Sampler through Edit &gt; Preferences &gt; Plugins and Scripts. To learn more about managing plugins, go [here](../../scripting-and-development/manage-installed-plugins/manage-installed-plugins-and-scripts.md).

## Python

The code below is the full python file for the autosave plugin. Below is a brief description of what the code is doing, but the code also includes comments with more information:

1. Import relevant modules.
   1. Qt is a multiplatform GUI toolkit. QtcCore, QtQml, and QtQuick are modules that we use to communicate between autosave.py and autosave.qml.
1. Define a method **save()** that saves the project every X minutes.
1. Create an autosave class. This class specifies how the **save()** method connects to the plugin UI so that parameters can change the behavior of the plugin
1. Define a method **register\_qml\_type()** that performs the setup for the plugin.
1. Call the plugin from within Sampler.

### autosave.py

```

## Import QT & QML modules to create the UI

from PySide2 import QtCore, QtQml, QtQuick 

## Import Sampler API

import substance_sampler as ssa 

## Import other modules for this specific example

import datetime 

import os 

import threading 

 

 

## Save the project every X minutes

def save(interval): 

    global t 

    ssa.save_project() 

    if ssa.save_project(): 

        now = datetime.datetime.now() 

        print("Autosave: %d:%d:%d" % (now.hour, now.minute, now.second)) 

    t = threading.Timer(interval, save, [interval]) 

    t.start() 

 

 

t = None 

 

 

## Declare the API AutoSave

class AutoSave(QtQuick.QQuickItem): 

    def __init__(self, parent=None): 

        super(AutoSave, self).__init__(parent) 

 

## Declare a first API function

## This function can be called from the QML file

## with 2 arguments, one string and one integer

    @QtCore.Slot(str, int) 

    def start_auto_save(self, default_path, interval): 

        if not ssa.save_project(): 

            ssa.save_project_as(os.path.join(default_path, "autosave.ssa")) 

        global t 

        t = threading.Timer(10, save, [interval]) 

        t.start() 

        print("Launch Autosave") 

 

## Second function of the API

## With no argument

    @QtCore.Slot(None) 

    def stop_auto_save(self): 

        global t 

        t.cancel() 

        print("Stop Autosave") 

 

 

## Function to declare the API and the panel

## First argument is Python class of your API

## Second argument is name of the API you will use in the QML file

## Third and fourth is the API version. In this case, 1.0

## Last is the name of the panel in Sampler UI

def register_qml_type(): 

    QtQml.qmlRegisterType(AutoSave, "AutoSave", 1, 0, "AutoSave") 

 

 

## Execute the plugin in Sampler UI thread

ssa.run_in_main_thread(register_qml_type)
```


## QML

The QML file defines the UI of the plugin. QML stands for Qt Markup Language and behaves similarly to other markup languages like HTML and XML. You can [learn more about QML here](https://doc.qt.io/qt-6/qmlapplications.html#:~:text=QML%20is%20a%20user%20interface%20specification%20and%20programming,imperative%20JavaScript%20expressions%20combined%20with%20dynamic%20property%20bindings.).

The general structure of autosave.qml is as follows:

1. Import modules.
   1. The Qt modules imported are necessary for the UI elements used in the file.
   1. The Autosave API class created in **autosave.py** is also imported. The QML file references this class on line 20.
1. Create variables that need to be tracked.
   1. **autoSaveFolder** is the folder where the Sampler file will be autosaved to.
   1. **timing** is the amount of time in seconds between autosaves.
   1. **textColor** is used so that the color of text in the plugin UI can be updated in a single place.
1. Instantiate the Python API
1. Define the UI.
   1. This includes hooks to the python API created in **autosave.py**. For example:
      1. Line 47 updates the **timing** variable value within the QML file whenever the "Autosave every (min):" element is changed.
      1. Line 64 calls the **start\_auto\_save** function from the API and passes the **timing**and **autoSaveFolder** variables as parameters.
1. Create a method to clean up the default filepath.

### autosave.qml

```

/* 

Import Qt modules to design the UI 

https://doc.qt.io/qt-5/qtqml-syntax-basics.html 

*/ 

import QtQuick 2.15 

import QtQuick.Controls 2.15 

import Qt.labs.platform 1.1 

import AutoSave 1.0 // Import API defined in the Python file 

 

Rectangle { 

  id: root 

  anchors.fill: parent 

  color: "#333333" 

 

  property var autoSaveFolder: removeQmlFilePathPrefix(StandardPaths.writableLocation(StandardPaths.DocumentsLocation)) 

  property var timing: 300 

  property var textColor: "#b3b3b3" 

 

  AutoSave { 

      id: api // Instantiate the Python API 

  } 

 

  Column { 

    id: controls 

    anchors.top: parent.top + 10 

    anchors.left: parent.left + 10 

    anchors.right: parent.right 

    width: parent.width 

    spacing: 20 

    leftPadding: 10 

    topPadding: 10 

 

    Column { 

        spacing: 5 

        Text { 

            id: timingTitle 

            text: "Autosave every (min): " 

            color: root.textColor 

        } 

        SpinBox { 

            id: timingControl 

            from: 1 

            to: 10 

            stepSize: 1 

            value: 5 

 

            onValueModified: ()=>{ 

                root.timing = timingControl.value * 60 

            } 

        } 

    } 

    Row { 

        Text { 

            text: "Off" 

            color: root.textColor 

            anchors.verticalCenter: toggle.verticalCenter 

        } 

        Switch { 

            id: toggle 

            checked: false 

 

            onClicked: ()=>{ 

                if (checked === true) { 

                    api.start_auto_save(root.autoSaveFolder, root.timing) // Call a function of the API with 2 arguments 

                } 

                else if (checked === false) { 

                    api.stop_auto_save() // Call a function of the API 

                } 

            } 

        } 

        Text { 

            text: "On" 

            color: root.textColor 

            anchors.verticalCenter: toggle.verticalCenter 

        } 

 

    } 

    Column { 

        spacing: 5 

        Text { 

            text: "Default Autosave Path" 

            color: root.textColor 

            } 

        Row { 

            id: folderInput 

            TextField { 

                id: folderText 

                text: root.autoSaveFolder 

                readOnly: true 

            } 

            Button { 

                id: folderSelection 

                text: qsTr("...") 

                width: 40 

                onClicked: ()=>{ 

                    folderDialog.open() 

                    } 

            } 

        } 

    } 

 

    FolderDialog { 

        id: folderDialog 

 

        onAccepted: ()=>{ 

            root.autoSaveFolder = removeQmlFilePathPrefix(folderDialog.currentFolder) 

        } 

    } 

 

  } 

      function qmlFilePathPrefix() { 

        if (Qt.platform.os === "windows") { 

            return "file:///" 

        } 

        return "file://" 

    } 

    function removeQmlFilePathPrefix(filePath) { 

        var prefix = qmlFilePathPrefix() 

        return filePath.toString().replace(prefix, '') 

    } 

}
```


## SVG

You may have noticed that **autosave.svg**is not explicitly called or mentioned in either **autosave.py**or **autosave.qml**. This is because Sampler looks for an SVG file with the same name as the PY file and automatically uses it as the plugin icon.

>[!NOTE]
>
> If your plugin folder contains an SVG with a filename that doesn't match the plugin's PY file, your plugin will not include an icon. This can create the appearance that your plugin hasn't appeared in the Sampler UI. If this is the case, move your cursor over Sampler's right bar to highlight your plugin.
> 
> Your browser does not support the HTML5 video element

If your plugin folder doesn't contain an SVG file, a default plugin icon will be used instead.

Below is an example SVG you can use for the autosave plugin created above.

[autosave.svg](https://helpx.adobe.com/content/dam/help/en/substance-3d/documentation/sadoc/files/234455541/234455542/1/1662460696349/autosave.svg)

## Limitations of the autosave plugin

The autosave plugin created above is functional, but it isn't perfect. For example, adjusting the autosave interval after autosave has been enabled will not actually change the time between autosaves - you would need to disable and reenable autosave for the value in the UI to be sent to the API.

If you are new to working with Python and QML together, fixing this bug is a useful way to build an understanding of how the different parts of the plugin communicate with each other.
