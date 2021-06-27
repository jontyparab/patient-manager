const tableRows = document.getElementsByClassName('data')
let oldTarget;
for (i = 0; i < tableRows.length; i++) {
    // console.log(i, v)
    tableRows[i].addEventListener('click', function (e) {
        oldTarget?.classList.remove('highlight')
        if (oldTarget === e.currentTarget) {
            oldTarget.classList.remove('highlight')
            oldTarget = null;
            return null;
        }
        e.currentTarget.classList.add('highlight')
        oldTarget = e.currentTarget
    })
    tableRows[i].style.setProperty("animation-delay", 0.01 * i + 's')
}
// console.log(tableRows)