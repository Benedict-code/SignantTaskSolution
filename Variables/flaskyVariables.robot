*** Settings ***
Documentation       Flasky Variables
Library             SeleniumLibrary


*** Variables ***
${URL}              http://192.168.1.162:8080/
${BROWSER}          chrome
${Reg_link}         xpath:/html/body/nav/ul/li[1]/a
${usernaame}         id:username
${passwoord}         id:password
${firstname}        id:firstname
${lastname}         id:lastname
${mobile}           id:phone
${Reg_button}       xpath:/html/body/section/form/input[6]
${Login_link}       xpath://a[contains(text(),'Log In')]
${Login}            xpath:/html/body/section/form/input[3]
${RowColumn}        xpath://table[@id='content']/tbody/tr[4]/td[2]
${C_count}          xpath://table[@id='content']/tbody/tr
${R_count}          xpath://table[@id='content']/tbody/tr/th
${tableH}           xpath://table[@id='content']
${tableC}           xpath://table[@id='content']
${tableR}           xpath://table[@id='content']
${tableCell}        xpath://table[@id='content']
