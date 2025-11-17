import re
from playwright.sync_api import Page, expect

def navigate_to_page(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

def test_expect_page_to_have_title(page: Page):
    navigate_to_page(page)
    #Expect a title "to contain" a substring
    expect(page).to_have_title("Agile helper")
    #expect(page).to_have_title(re.compile("Agile helper")) , med reg ex compiler

#US1 - se userstory.txt för userstory och scenario.
#Testa att det går att det går att se sprint planning
def test_view_sprint_planning(page: Page):
    #Anropar en tidigare definierad funktion som används många gånger för att navigera till websidan
    navigate_to_page(page)
    #klicka på knappen "First"
    first_button=page.get_by_role("button").get_by_text("Första")
    first_button.click()

    # Hitta button med texten "Sprint planning"
    # Testet letar efter en knapp med texten ”Sprint planning”. Testet förväntar sig att knappen verkligen syns
    sp_button = page.get_by_role("button").get_by_text("Sprint planning", exact=False)
    expect(sp_button).to_be_visible()

    # Klicka på den
    sp_button.click()

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

#US2
#Testa att det går att klicka på knappen för att avsluta sprintplaneringen och naviering därefter fungerar

def test_finish_sprint_planning(page: Page):
    navigate_to_page(page)

    #Klicka på knappen "Första" (exakt text, endast svenska versionen)
    first_button=page.get_by_role("button").get_by_text("Första")
    first_button.click()

 # Hitta button med texten "Sprint planning"
    # Testet letar efter en knapp med texten ”Sprint planning”. Testet förväntar sig att knappen verkligen syns
    sp_button = page.get_by_role("button").get_by_text("Sprint planning", exact=False)
    expect(sp_button).to_be_visible()

    # Klicka på den
    sp_button.click()

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

    planning_finish_button = page.get_by_role("button").get_by_text("Nu är vi klara", exact=False)
    planning_finish_button.click()

    expect(page.get_by_role("button").get_by_text("Sprint planning", exact=False)).to_be_visible()

#US3
#Testa att det går att komma åt "Daily Standup" genom valet "Första" som alternativ

def test_daily_standup_from_first(page: Page):
    navigate_to_page(page)

    first_button=page.get_by_role("button").get_by_text("Första")
    first_button.click()

    daily_button = page.get_by_role("button").get_by_text("Daily standup", exact=False)
    daily_button.click()

    heading = page.get_by_role("heading").get_by_text("Daily standup")

    expect(heading).to_be_visible()


#US4
#Testa att det går att gå att använda "Välj dag" för att gå tillbaka till webbsidans startsida

#Klicka på Knappen “Första”
def test_return_to_main_page(page: Page):
    navigate_to_page(page)
    first_button = page.get_by_role("button", name="Första")
    first_button.click()

    #Kontrollera att knappen "Välj dag" finns
    ret_button = page.get_by_role("button", name="Välj dag")
    expect(ret_button).to_be_visible()

    #Klicka på knappen
    ret_button.click()

    #Kontrollera att du kommer tillbaka till startsidan
    first_button = page.get_by_role("button", name="Första")
    expect(first_button).to_be_visible()

#US5
#Testa att det går att välja "Daily Standup" från "Någonstans mitt i" knappen

def test_daily_standup_dialog(page: Page):
    #Navigera till webbsidan
    navigate_to_page(page)

    #Klicka på knappen med texten ”Någonstans mitt i”
    page.get_by_role("button", name="Någonstans mitt i").click()

    #Klicka på knappen med texten ”Daily standup”
    page.get_by_role("button").get_by_text("Daily standup").click()

    #Hittar ett element med rollen dialog <dialog> och matchar sedan text inuti dialogen
    dialog_heading_daily = page.get_by_role("heading", name="Daily standup")
    expect(dialog_heading_daily).to_be_visible()

#US6
#Testa att det går att navigera till "Daily standup" och starta timer för Daily Standup

def test_daily_standup_timer(page: Page):
    # Klicka på knappen "Någonstans mitt i"
    navigate_to_page(page)
    second_button = page.get_by_role("button", name="Någonstans mitt i")
    second_button.click()
    
    # Klicka på knappen "Daily standup"
    daily_standup_button = page.get_by_role("button").get_by_text("Daily standup")
    daily_standup_button.click()
    
    # Kontrollera att dialog visas med rubrik "Daily Standup"
    dialog_heading_daily = page.get_by_role("heading", name="Daily standup")
    expect(dialog_heading_daily).to_be_visible()
    
    # Kontrollera att knappen "Börja mötet" visas
    start_timer = page.get_by_role("button").get_by_text("Börja mötet")
    expect(start_timer).to_be_visible()
    
    # Klicka på knappen och verifiera att tid startar
    start_timer.click()

#US7
#Testa att knappen "Nu är mötet slut" stänger dialogen för Daily standup och du navigerar tillbaka till menyn

def test_close_daily_standup_dialog(page: Page):
    navigate_to_page(page)

    second_button=page.get_by_role("button").get_by_text("Någonstans mitt i")
    second_button.click()

    # Klicka på knappen "Daily standup"
    daily_standup_button = page.get_by_role("button").get_by_text("Daily standup")
    daily_standup_button.click()
    
    # Kontrollera att dialog visas med rubrik "Daily Standup"
    dialog_heading_daily = page.get_by_role("heading", name="Daily standup")
    expect(dialog_heading_daily).to_be_visible()

    close_button = page.get_by_role("button").get_by_text("Nu är mötet slut!", exact=False)
    close_button.click()

    expect(page.get_by_role("button").get_by_text("Daily standup", exact=False)).to_be_visible()

#US8
#Testar att daily standup även går att komma åt via sista veckan i sprinten

def test_daily_standup_from_button_last(page: Page):
    navigate_to_page(page)

    third_button = page.get_by_role("button", name="Sista")
    third_button.click()

    daily_standup_button = page.get_by_role("button").get_by_text("Daily standup")
    daily_standup_button.click()

    dialog_heading_daily = page.get_by_role("heading", name="Daily standup")
    expect(dialog_heading_daily).to_be_visible()


#US9
#Testa att det går att komma till Sprint Review texten och gå tillbaka därifrån

def test_sprint_review_dialog(page: Page):
    navigate_to_page(page)
    third_button = page.get_by_role("button", name="Sista")
    third_button.click()

    #Klicka på knappen "Presentera ert arbete för produktägaren under Sprint Review"
    sprint_review_button = page.get_by_role("button").get_by_text("Sprint review")
    sprint_review_button.click()

    dialog_heading_review = page.get_by_role("heading", name="Sprint review")
    expect(dialog_heading_review).to_be_visible()

    #Klickar på knappen är reviewn är klar och går tillbaka till föregående meny
    done_button = page.get_by_role("button").get_by_text("Ok vi är klara")
    done_button.click()

    #Verifierar att vi kommer tillbaka till tidigare sida
    expect(page.get_by_role("button").get_by_text("Sprint review", exact=False)).to_be_visible()

#US10
#Testa att det går att komma till Sprint retrospective dialogen och läsa informationen

def test_sprint_retrospective_dialog(page: Page):
    navigate_to_page(page)
    third_button = page.get_by_role("button", name="Sista")
    third_button.click()

    #Klickar på knappen för sprint retrospective
    retrospective_button = page.get_by_role("button").get_by_text("Sprint retrospective", exact=False)
    retrospective_button.click()

    #Verifierar att en dialog öppnas 

    dialog_heading_retro = page.get_by_role("heading", name="Sprint retrospective")
    expect (dialog_heading_retro).to_be_visible()

#US11
#Testa att det går att komma ur sprint retrospective dialogen och navigera tillbaka
def test_close_sprint_retrospective_dialog(page: Page):
    # Navigera till startsidan
    navigate_to_page(page)

    # Klicka på knappen “Sista”
    page.get_by_role("button", name="Sista").click()

    # Klicka på knappen “Avsluta sprinten med att utvärdera ert arbete i Sprint retrospective”
    retrospective_button = page.get_by_role("button").get_by_text("Sprint retrospective", exact=False)
    retrospective_button.click()

    # Kontrollera att dialogen öppnas (kolla rubriken)
    dialog_heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(dialog_heading).to_be_visible()

    # Klicka på knappen “Sprinten är färdig”
    finished_button = page.get_by_role("button").get_by_text("Sprinten är färdig", exact=False)
    finished_button.click()

    # Verifiera att användaren hamnar tillbaka på föregående sida
    # Vi kontrollerar att Retrospective-knappen syns igen.
    expect(page.get_by_role("button").get_by_text("Sprint retrospective", exact=False)).to_be_visible()
