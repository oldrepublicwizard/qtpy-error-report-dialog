"""Error report dialogs (Qt + Tk)."""
from qtpy_error_report_dialog.base import ErrorReportData, ErrorReportDialogBase

__all__ = ["ErrorReportData", "ErrorReportDialogBase", "QtErrorReportDialog", "TkErrorReportDialog"]

def __getattr__(name: str):
    if name == "QtErrorReportDialog":
        from qtpy_error_report_dialog.qt_dialog import QtErrorReportDialog
        return QtErrorReportDialog
    if name == "TkErrorReportDialog":
        from qtpy_error_report_dialog.tk_dialog import TkErrorReportDialog
        return TkErrorReportDialog
    raise AttributeError(name)
