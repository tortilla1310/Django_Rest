import React from 'react'

const FooterItem = ({footer}) => {
    return (
        <tr>
            <td>
                {footer.about_company}
            </td>
            <td>
                {footer.contact_details}
            </td>
            <td>
                {footer.copyright}
            </td>
        </tr>
    )
}

const FooterList = ({footers}) => {
    return (
        <table>
            <th>
                О компании
            </th>
            <th>
                Контактная информация
            </th>
            <th>
                Аворсике права
            </th>
            {footers.map((footer) => <FooterItem footer={footer}/>)}
        </table>
    )
}

export default FooterList