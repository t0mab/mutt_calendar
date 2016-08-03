# mutt_calendar

Command line tool to display calendar in mutt.

# Command line usage
./cal.py filename.ics

# Mutt usage

## Add to .mailcap file:
text/calendar; path/mutt_calendar/cal.py '%s'; nametemplate=%s.ics; copiousoutput;

## Add to .muttrc file:
auto_view text/calendar
