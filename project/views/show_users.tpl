<h1>Show me the users</h1>

<table>
    <tbody>
        <tr><th>Email</th><th>Password</th><th>CPF</th><th>Data hora</th></tr>
        %for row in rows:
        <tr>
        %for col in row:
            <td>{{col}}</td>
        %end
        </tr>
    %end
    <tbody>
</table>