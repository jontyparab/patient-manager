const tableRows = document.getElementsByClassName('data')
let oldTarget;
for (let row of tableRows) {
    // console.log(row)
    row.addEventListener('click', function (e) {
        oldTarget?.classList.remove('highlight')
        e.currentTarget.classList.toggle('highlight')
        oldTarget = e.currentTarget
    })
}
// console.log(tableRows)