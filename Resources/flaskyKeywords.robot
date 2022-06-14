*** Settings ***
Documentation       Flasky Keywords
Library             SeleniumLibrary
Library             FakerLibrary
Resource            ../Variables/flaskyVariables.robot


*** Keywords ***
RegisterUser
            Open Browser      ${URL}         ${BROWSER}
            Maximize Browser Window
            Page Should Contain    index page
            Wait Until Element Is Visible    ${Reg_link}
            Click Link        ${Reg_link}
            ${usernamee}=     FakerLibrary.User Name
            Input Text        ${usernaame}    ${usernamee}
            Input Text        ${passwoord}     passwordd
            Wait Until Element Is Visible     ${firstname}
            ${firstnamee}=    FakerLibrary.First Name
            Input Text        ${firstname}    ${firstnamee}
            ${lastnamee}=     FakerLibrary.lastname
            Input Text        ${lastname}     ${lastnamee}
            Input Text        ${mobile}       +358400000000
            Wait Until Element Is Visible     ${Reg_button}
            Click Button      ${Reg_button}


UserLogin
            Open Browser       ${URL}      ${BROWSER}
            Maximize Browser Window
            Page Should Contain    index page
            Wait Until Element Is Visible   ${Login_link}
            Click Link        ${Login_link}
            Input Text        ${usernaame}    usernamee
            Input Text        ${passwoord}    passwordd
            Wait Until Element Is Visible    ${Login}
            Click Button      ${Login}
            Page Should Contain    User Information

User Information
            Open Browser    ${URL}   ${BROWSER}
            Maximize Browser Window
            Page Should Contain    index page
            Wait Until Element Is Visible    ${Login_link}
            Click Link      ${Login_link}
            Input Text      ${usernaame}    usernamee
            Input Text      ${passwoord}    passwordd
            Wait Until Element Is Visible    ${Login}
            Click Button    ${Login}
            Page Should Contain    User Information
            ${UI_row_column}=    Get Text    ${RowColumn}
            Log To Console    ${UI_row_column}
            ${Column}=  Get Element Count    ${C_count}
            Log To Console    ${Column}
            ${Row}=     Get Element Count    ${R_count}
            Log To Console    ${Row}
            Set Selenium Speed    1
            Table Header Should Contain    ${tableH}       key
            Table Column Should Contain    ${tableC}       2    +358400000000
            Table Row Should Contain       ${tableR}       3    firstnamee
            Table Cell Should Contain      ${tableCell}    2    2     usernamee




            