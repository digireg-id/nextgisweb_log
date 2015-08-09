<%inherit file='nextgisweb:templates/base.mako' />

<table class="pure-table pure-table-horizontal" style="width: 100%;">
    <thead>
        <tr>
            <th style="width: 4em;">ID</th>
            <th style="width: 20em;">Append DT</th>
            <th style="width: 10em">Component</th>
            <th style="width: 10em;">Group</th>
            <th style="width: 10em;">Level</th>
            <th style="width: 10em;">Mess Name</th>
            <th style="width: 80em;">Mess Text</th>
            <th style="width: 0px;">&nbsp;</th>
        </tr>
    </thead>
    <tbody>
        %for obj in obj_list:
            <tr>
                <td>${obj.id}</td>
                <td>${obj.append_dt}</td>
                <td>${obj.component}</td>
                <td>${obj.group}</td>
                <td>${obj.message_level_name}</td>
                <td>${obj.message_name}</td>
                <td>${obj.message_text}</td>
                <td>
                    <a class="dijitIconSearch" style="width: 16px; height: 16px; display: inline-block;" href="${request.route_url('log.message.info', id=obj.id)}"></a>
                </td>
            </tr>
        %endfor
    </tbody>
</table>