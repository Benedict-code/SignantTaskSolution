*** Settings ***
Documentation       Flasky TestCases
Library             SeleniumLibrary
Library             FakerLibrary
Resource            ../Resources/flaskyKeywords.robot
Resource            ../Variables/flaskyVariables.robot
Suite Teardown      Close All Browsers


*** Test Cases ***
TC1
    RegisterUser
    [Tags]     User Registration Testing
TC2
    UserLogin
    [Tags]     User Login Testing
TC3
    User Information
    [Tags]     User Information Review Testing

TC4
    [Tags]          Invalid
    [Template]       DDT For Invalid Login Scenarios
    #username       Password            errormessage
    user            passwordd           Login Failure
    usernamee       test                Login Failure
    ${EMPTY}        passwordd           ${EMPTY}
    usernamee       ${EMPTY}            ${EMPTY}
    user            test                Login Failure

*** Keywords ***
DDT For Invalid Login Scenarios
    [Arguments]     ${username}      ${password}        ${errormessage}
    Open Browser      ${URL}         ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible     ${Login_link}
    Click Link      ${Login_link}
    Input Text     ${usernaame}      ${username}
    Input Text     ${passwoord}      ${password}
    Wait Until Element Is Visible    ${Login}
    Click Button     ${Login}
    Page Should Contain    ${errormessage}



