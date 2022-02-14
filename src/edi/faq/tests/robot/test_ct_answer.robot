# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.faq -t test_answer.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.faq.testing.EDI_FAQ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/faq/tests/robot/test_answer.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Answer
  Given a logged-in site administrator
    and an add Question form
   When I type 'My Answer' into the title field
    and I submit the form
   Then a Answer with the title 'My Answer' has been created

Scenario: As a site administrator I can view a Answer
  Given a logged-in site administrator
    and a Answer 'My Answer'
   When I go to the Answer view
   Then I can see the Answer title 'My Answer'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Question form
  Go To  ${PLONE_URL}/++add++Question

a Answer 'My Answer'
  Create content  type=Question  id=my-answer  title=My Answer

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Answer view
  Go To  ${PLONE_URL}/my-answer
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Answer with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Answer title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
