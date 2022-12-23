import React from 'react'

const MenuItem = ({menu}) => {
    return (
        <tr>
            <td>
                {menu.home}
            </td>
            <td>
                {menu.contacts}
            </td>
            <td>
                {menu.service}
            </td>
        </tr>
    )
}

const MenuList = ({menus}) => {
    return (
        <table>
            <th>
                home
            </th>
            <th>
                contacts
            </th>
            <th>
                service
            </th>
            {menus.map((menu) => <MenuItem menu={menu}/>)}
        </table>
    )
}

export default MenuList