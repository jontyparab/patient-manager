const tableRows = document.getElementsByClassName('data')
let oldTarget;
for (let row of tableRows) {
    // console.log(row)
    row.addEventListener('click', function (e) {
        oldTarget?.classList.remove('highlight')
        if (oldTarget === e.currentTarget) {
            oldTarget.classList.remove('highlight')
            oldTarget = null;
            return null;
        }
        e.currentTarget.classList.add('highlight')
        oldTarget = e.currentTarget
    })
}
// console.log(tableRows)