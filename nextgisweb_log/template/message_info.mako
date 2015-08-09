<%inherit file='nextgisweb:templates/base.mako' />

<table width="100%" class="pure-table pure-table-horizontal" cellspacing="1">
    <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>ID</label>
        </td>
        <td class="tableContainer-valueCell">
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.id}</div>
        </td>
    </tr>
    <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Append DT</label>
        </td>
        <td class="tableContainer-valueCell">
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.append_dt}</div>
        </td>
    </tr>
        <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Component</label>
        </td>
        <td class="tableContainer-valueCell">
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.component}</div>
        </td>
    </tr>
    </tr>
        <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Group</label>
        </td>
        <td class="tableContainer-valueCell">
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.group}</div>
        </td>
    </tr>
    </tr>
    <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Level</label>
        </td>
        <td class="tableContainer-valueCell">
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.message_level_name}</div>
        </td>
    </tr>
    <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Mess Name</label>
        </td>
        <td class="tableContainer-valueCell">
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.message_name}</div>
        </td>
    </tr>

    <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Mess Text</label>
        </td>
            <div class="dijit dijitReset dijitInline dijitLeft dijitTextBox dijitValidationTextBox">${obj.message_text}</div>
        </td>
    </tr>

     <tr>
        <td class="tableContainer-labelCell" style="width: 150px;">
            <label>Exception</label>
        </td>
        <td class="tableContainer-valueCell" >
            <textarea dojoType="dijitTextArea" style="height: 40em; width: 100%">${obj.exc_info}</textarea>
        </td>
    </tr>
</table>