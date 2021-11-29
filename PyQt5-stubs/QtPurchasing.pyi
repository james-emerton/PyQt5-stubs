# The PEP 484 type hints stub file for the QtPurchasing module.
#
# Generated by SIP 6.3.1
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQtPurchasing.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

from PyQt5 import sip
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QInAppProduct(QtCore.QObject):

    class ProductType(int):
        Consumable = ... # type: QInAppProduct.ProductType
        Unlockable = ... # type: QInAppProduct.ProductType

    Consumable = ...  # type: QInAppProduct.ProductType
    Unlockable = ...  # type: QInAppProduct.ProductType

    def purchase(self) -> None: ...
    def description(self) -> str: ...
    def title(self) -> str: ...
    def price(self) -> str: ...
    def productType(self) -> 'QInAppProduct.ProductType': ...
    def identifier(self) -> str: ...


class QInAppStore(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def transactionReady(self, transaction: 'QInAppTransaction') -> None: ...
    def productUnknown(self, productType: QInAppProduct.ProductType, identifier: str) -> None: ...
    def productRegistered(self, product: QInAppProduct) -> None: ...
    def setPlatformProperty(self, propertyName: str, value: str) -> None: ...
    def registeredProduct(self, identifier: str) -> QInAppProduct: ...
    def registerProduct(self, productType: QInAppProduct.ProductType, identifier: str) -> None: ...
    def restorePurchases(self) -> None: ...


class QInAppTransaction(QtCore.QObject):

    class FailureReason(int):
        NoFailure = ... # type: QInAppTransaction.FailureReason
        CanceledByUser = ... # type: QInAppTransaction.FailureReason
        ErrorOccurred = ... # type: QInAppTransaction.FailureReason

    NoFailure = ...  # type: QInAppTransaction.FailureReason
    CanceledByUser = ...  # type: QInAppTransaction.FailureReason
    ErrorOccurred = ...  # type: QInAppTransaction.FailureReason

    class TransactionStatus(int):
        Unknown = ... # type: QInAppTransaction.TransactionStatus
        PurchaseApproved = ... # type: QInAppTransaction.TransactionStatus
        PurchaseFailed = ... # type: QInAppTransaction.TransactionStatus
        PurchaseRestored = ... # type: QInAppTransaction.TransactionStatus

    Unknown = ...  # type: QInAppTransaction.TransactionStatus
    PurchaseApproved = ...  # type: QInAppTransaction.TransactionStatus
    PurchaseFailed = ...  # type: QInAppTransaction.TransactionStatus
    PurchaseRestored = ...  # type: QInAppTransaction.TransactionStatus

    def status(self) -> 'QInAppTransaction.TransactionStatus': ...
    def platformProperty(self, propertyName: str) -> str: ...
    def finalize(self) -> None: ...
    def timestamp(self) -> QtCore.QDateTime: ...
    def errorString(self) -> str: ...
    def failureReason(self) -> 'QInAppTransaction.FailureReason': ...
    def orderId(self) -> str: ...
    def product(self) -> QInAppProduct: ...


PYQT_PURCHASING_VERSION = ... # type: int
PYQT_PURCHASING_VERSION_STR = ... # type: str
QTPURCHASING_VERSION = ... # type: int
QTPURCHASING_VERSION_STR = ... # type: str
